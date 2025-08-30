import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, ModelSettings, function_tool
from openai import AsyncOpenAI
import asyncio


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise Exception("GEMINI_API_KEY is not set")


gemini_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=gemini_client,
)

@function_tool
def get_weather(location: str) -> str:
    """Get the current weather in a given location."""
    return f"The weather in {location} is sunny."

@function_tool
def calculator() -> int:
    """Calculate the sum of two numbers."""
    return 2 + 2

base_agent = Agent(
    name="Base Agent",
    instructions="You are a helpful assistant.",
    model=model,
    model_settings=ModelSettings(
        temperature=0.4,
        max_tokens=500,
        tool_choice="required"
    ),
    tools=[get_weather]
)

# Cloning Agent from base agent with different instructions
creative_agent = base_agent.clone(
    name="CreativeAssistant",
    instructions="You are a creative writing assistant. Always respond in a creative writing style.",
    model_settings=ModelSettings(
        temperature=0.9, # Override model settings
        max_tokens=500,
    ),
    tools=[calculator]
)

# What happens:
# ✅ New agent object created
# ✅ New name and instructions
# ✅ Same tools list (shared reference)
# ✅ Same model settings (unless overridden)


result1 =  Runner.run_sync(
    base_agent,
    "What is 2 + 2?",
)

print("\nBase Agent Response: ",result1.final_output)

result2 =  Runner.run_sync(
    creative_agent,
    "What is weather in New York?",
)

print("\nCreative Agent Response: ",result2.final_output)




