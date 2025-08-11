import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool, ModelSettings
from openai import AsyncOpenAI

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

def main():
    """Learn Model Settings with simple examples."""
    # 🎯 Example 1: Temperature (Creativity Control)
    print("\nTemperature Settings")
    print("-" * 30)

    agent_cold = Agent(
        name="Cold Agent",
        instructions="You are a helpful assistant.",
        model=model,
        model_settings=ModelSettings(temperature=0.1),
    )

    agent_hot = Agent(
        name="Hot Agent",
        instructions="You are a helpful assistant.",
        model_settings=ModelSettings(temperature=1.9),
        model=model
    )

    question = "Tell me about AI in 2 sentences"

    print("Cold Agent (Temperature = 0.1):")
    result_cold = Runner.run_sync(agent_cold, question)
    print(result_cold.final_output)

    print("\nHot Agent (Temperature = 1.9):")
    result_hot = Runner.run_sync(agent_hot, question)
    print(result_hot.final_output)

    print("\n💡 Notice: Cold = focused, Hot = creative")
    print("📝 Note: Gemini temperature range extends to 2.0")


if __name__ == "__main__":
    main()