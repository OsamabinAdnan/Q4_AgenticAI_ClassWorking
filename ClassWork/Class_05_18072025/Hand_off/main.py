# Import necessary libraries for asynchronous programming, environment variables, and agent framework
import asyncio
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from openai import AsyncOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Disable tracing for the application
set_tracing_disabled(True)

# Retrieve the Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")
# Check if the API key is set, raise an error if not
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

# Initialize the AsyncOpenAI client with the Gemini API key and base URL
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Create a model instance using the Gemini 2.0 Flash model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)

# Define an agent for translating text to Urdu
urdu_translator = Agent(
    name="Urdu Translator",
    instructions="You are a helpful translator that translates text to Urdu.",
    model=model,
)
    
# Define an agent for translating text to Arabic
arabic_translator = Agent(
    name="Arabic Translator",
    instructions="You are a helpful translator that translates text to Arabic.",
    model=model,
)
    
# Define an agent for translating text to French
french_translator = Agent(
    name="French Translator",
    instructions="You are a helpful translator that translates text to French.",
    model=model,
)

# Define the main asynchronous function to handle translation requests
async def main():
    # Create a main agent that delegates translation tasks to specific language translators
    main_agent = Agent(
        name="Main Agent",
        instructions="""
        You have to take the user's input and call the appropriate handoff to translate the user's input.
        If you don't find appropriate handoff than simply refuse the user.
        """,
        model=model,
        handoffs=[urdu_translator, arabic_translator, french_translator],
    )

    # Run the main agent with a sample input to translate "how are you" to Urdu
    result = await Runner.run(
        main_agent,
        input="Translate how are you in urdu",
    )

    # Print the final translation result
    print("Result:", result.final_output)

# Check if the script is run directly and execute the main function
if __name__ == "__main__":
    asyncio.run(main())