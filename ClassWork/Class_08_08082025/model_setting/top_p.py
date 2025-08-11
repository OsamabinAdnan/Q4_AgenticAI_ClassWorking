import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool, ModelSettings
from openai import AsyncOpenAI
from rich import print

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

print("\n🔧 Top_P Settings")
print("-" * 30)

def main():
    agent_100 = Agent(
            name="100% Top_P",
            instructions="You are a helpful assistant.",
            model_settings=ModelSettings(top_p=1.0),
            model=model
    )

    agent_90 = Agent(
            name="90% Top_P",
            instructions="You are a helpful assistant.",
            model_settings=ModelSettings(top_p=0.9),
            model=model
    )

    agent_60 = Agent(
        name="60% Top_P",
        instructions="You are a helpful assistant.",
        model_settings=ModelSettings(top_p=0.6),
        model=model
    )

    agent_30 = Agent(
        name="30% Top_P",
        instructions="You are a helpful assistant.",
        model_settings=ModelSettings(top_p=0.3),
        model=model
    )

    question = "What is the meaning of life? within 100 words"

    print("\n100% Top_P:")
    print("=" * 30)
    result_auto = Runner.run_sync(agent_100, question)
    print(result_auto.final_output)

    print("\n90% Top_P:")
    print("=" * 30)
    result_auto = Runner.run_sync(agent_90, question)
    print(result_auto.final_output)

    print("\n60% Top_P:")
    print("=" * 30)
    result_auto = Runner.run_sync(agent_60, question)
    print(result_auto.final_output)

    print("\n30% Top_P:")
    print("=" * 30)
    result_auto = Runner.run_sync(agent_30, question)
    print(result_auto.final_output)

    print("\ntop_p = 1.0 → No restriction; the model considers all tokens (behaves like normal sampling). Lower values (e.g., 0.9) → The model only considers the top 90% most probable tokens, discarding the long tail of unlikely options. Same is the case for 60 and 30%.\n")


if __name__ == "__main__":
    main()