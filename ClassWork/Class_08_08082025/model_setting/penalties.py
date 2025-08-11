import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, ModelSettings
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
    model="gemini-2.0-flash",
    openai_client=external_client
)

print("\n🔧 Frequency & Presence Penalties")
print("-" * 30)

def main():
    agent_1 = Agent(
            name="agent1",
            instructions="You are a helpful assistant.",
            model_settings=ModelSettings(
                top_p=0.3,              # Use only top 30% of vocabulary
                frequency_penalty=0.0, # Avoid repeating words | Default: 0.0
                presence_penalty=0.0, # Encourage new topics | Default: 0.0
            ),
            model=model
    )

    agent_2 = Agent(
            name="agent2",
            instructions="You are a helpful assistant.",
            model_settings=ModelSettings(
                top_p=0.3,              # Use only top 30% of vocabulary
                frequency_penalty=1.0, # Avoid repeating words | Default: 0.0
                presence_penalty=1.0, # Encourage new topics | Default: 0.0
            ),
            model=model
    )


    question = "What is the meaning of life? within 100 words"

    print("\nBoth values set to 0.0:")
    print("=" * 30)
    result_default = Runner.run_sync(agent_1, question)
    print(result_default.final_output)
    # print(result_default)

    print("\nBoth values set to 1.0:")
    print("=" * 30)
    result_modified = Runner.run_sync(agent_2, question)
    print(result_modified.final_output)
    # print(result_modified)


if __name__ == "__main__":
    main()