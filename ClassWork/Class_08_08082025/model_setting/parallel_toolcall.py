import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, ModelSettings, function_tool
from openai import AsyncOpenAI
from rich import print
import random
import asyncio

# 🌿 Load environment variables from .env file
load_dotenv()

# 🚫 Disable tracing for clean output (optional for beginners)
set_tracing_disabled(disabled=True)

# 🔐 1) Environment & Client Setup
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # 🔑 Get your API key from environment
BASE_URL ="https://generativelanguage.googleapis.com/v1beta/openai/"  # 🌐 Gemini-compatible base URL (set this in .env file)

# 🌐 Initialize the AsyncOpenAI-compatible client with Gemini details
external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL
)

# 🧠 2) Model Initialization
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

print("\n🔧 Parallel Tool Calls")
print("-" * 30)

@function_tool
def weather_tool(city: str) -> dict:
    """
    Weather tool that returns random weather data.
    """
    return {
        "city": city,
        "temperature": round(random.uniform(15, 35), 1),
        "condition": random.choice(["Sunny", "Cloudy", "Rainy", "Windy"]),
        "humidity": random.randint(20, 90)
    }

@function_tool
def calculator(expression: str) -> float:
    """
    Calculator that pretends to evaluate math expressions.
    """
    # Just a fake result to simulate calculation
    return 42.0

@function_tool
def translator(text: str, target_language: str) -> str:
    """
    Translator that appends the language code to the text.
    """
    return f"[{target_language.upper()}] {text}"

async def main():
    # Agent can use multiple tools at once
    parallel_agent = Agent(
        name="Multi-Tasker",
        tools=[weather_tool, calculator, translator],
        model_settings=ModelSettings(
            tool_choice="auto",
            parallel_tool_calls=True  # Use multiple tools simultaneously
        )
    )

    # Agent uses tools one at a time
    sequential_agent = Agent(
        name="One-at-a-Time",
        tools=[weather_tool, calculator, translator],
        model_settings=ModelSettings(
            tool_choice="auto",
            parallel_tool_calls=False  # Use tools one by one
        )
)

    print("\nParallel Tool Calls:")
    print("=" * 30)
    result_default = await Runner.run(parallel_agent, input="What is the weather in New York? and translate it into French")
    print(result_default.final_output)
    # print(result_default)

    print("\nSequential Tool Calls:")
    print("=" * 30)
    result_modified = await Runner.run(sequential_agent, input="What is the weather in New York? and calculate humidity and translate it into French")
    print(result_modified.final_output)
    # print(result_modified)

if __name__ == "__main__":
    asyncio.run(main())