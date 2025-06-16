"""
CLI Based Agent using Google's Gemini Model through OpenAI-compatible API
This script demonstrates the use of the Google Gemini model with an OpenAI-compatible interface
for creating a simple chatbot agent.
"""

from dotenv import load_dotenv
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
import asyncio

# Load environment variables from .env file
load_dotenv()

async def app():
    # Configuration for the Gemini model
    MODEL_NAME = "gemini-1.5-flash"
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

    # Validate API key existence
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable is not set.")
    
    # Initialize OpenAI-compatible client for Gemini API
    external_client = AsyncOpenAI(
        api_key=GEMINI_API_KEY,
        base_url=BASE_URL,
    )

    # Configure the chat model
    model = OpenAIChatCompletionsModel(
        model=MODEL_NAME,
        openai_client=external_client,
    )

    # Set up runtime configuration
    config = RunConfig(
        model=model,
        model_provider=external_client,
        tracing_disabled=True,
    )

    # Create an AI assistant with basic instructions
    assistant = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        model=model,
    )

    # Run the assistant with a test query about Pakistan
    result = await Runner.run(
        assistant,
        "Tell me something interesting about Pakistan.",
        run_config=config,
    )
    print(result.final_output)

if __name__ == "__main__":
    # Run the async application
    asyncio.run(app())
