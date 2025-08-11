import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool, ModelSettings
from openai import AsyncOpenAI
from rich import print
import asyncio

# 🌿 Load environment variables from .env file
load_dotenv()

# 🚫 Disable tracing for clean output (optional for beginners)
set_tracing_disabled(disabled=True)

# 🔐 1) Environment & Client Setup
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # 🔑 Get your API key from environment
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"  # 🌐 Gemini-compatible base URL (set this in .env file)

# 🌐 Initialize the AsyncOpenAI-compatible client with Gemini details
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL
)

# 🧠 2) Model Initialization
model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

print("\n🔧 Max Token Settings")
print("-" * 30)

agent_100 = Agent(
        name="max_tokens100",
        instructions="You are a helpful assistant.",
        model_settings=ModelSettings(max_tokens=100, temperature=0.8),
        model=model
)
agent_500 = Agent(
        name="max_tokens500",
        instructions="You are a helpful assistant.",
        model_settings=ModelSettings(max_tokens=500, temperature=0.8),
        model=model
)
agent_1000 = Agent(
    name="max_tokens1000",
    instructions="You are a helpful assistant.",
    model_settings=ModelSettings(max_tokens=1000, temperature=0.8),
    model=model
)
async def main():

    question = "What is the meaning of life?"

    print("\nMax Tokens = 100:")
    print("=" * 30)
    result100 = await Runner.run(agent_100, question)
    print(result100.final_output)
    
    print("\nMax Tokens = 500:")
    print("=" * 30)
    result200 = await Runner.run(agent_500, question)
    print(result200.final_output)

    print("\nMax Tokens = 1000:")
    print("=" * 30)
    result250 = await Runner.run(agent_1000, question)
    print(result250.final_output)



if __name__ == "__main__":
    asyncio.run(main())