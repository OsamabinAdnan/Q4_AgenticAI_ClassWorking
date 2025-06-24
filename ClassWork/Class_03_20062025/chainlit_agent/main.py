# Import required libraries
import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool
import asyncio
import chainlit as cl

# Load environment variables from .env file
load_dotenv()

# Disable tracing for better performance
set_tracing_disabled(True)  # Disable tracing for the agent

# Define a tool function for getting weather information
@function_tool
def get_weather(city: str) -> str:
    """
    Get the current weather for a given city.
    Args:
        city (str): Name of the city to get weather for
    Returns:
        str: Weather information for the specified city
    """
    # This is a placeholder implementation. Replace with actual weather API call.
    return f"The current weather in {city} is sunny with a temperature of 25°C."

# Initialize the chat application when a new session starts
@cl.on_chat_start
async def start():
    # Configure the AI model settings
    MODEL="gemini-2.0-flash"
    API_KEY = os.getenv("GEMINI_API_KEY")

    if not API_KEY:
        raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
    
    # Initialize OpenAI client with Gemini API configuration
    external_client = AsyncOpenAI(
        api_key=API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    # Set up the chat model
    model = OpenAIChatCompletionsModel(
        model=MODEL,
        openai_client=external_client,
    )

    # Initialize empty chat history for the session
    cl.user_session.set("chat_history", [])

    # Create the weather assistant agent
    weather_assistant = Agent(
        name="Weather Assistant",
        instructions=f"You are a helpful assistant that provides weather information for cities.",
        model=model,
        tools=[get_weather],  # Register the weather function as a tool
    )

    # Store the agent in the user session for later use
    cl.user_session.set("weather_assistant", weather_assistant)

    # Send welcome message to the user
    await cl.Message(
        content= "Welcome to the Weather Assistant! You can ask me about the weather in any city.",
    ).send()

# Handle incoming chat messages
@cl.on_message
async def main(message:cl.Message):
    # Show thinking message while processing
    msg = await cl.Message(content="Thinking...").send()
    
    # Retrieve the agent and chat history from the session
    assistant = cl.user_session.get("weather_assistant")
    history = cl.user_session.get("chat_history") or []

    # Add user message to chat history
    history.append(
        {
            "role": "user",
            "content": message.content
        }
    )

    # Process the message using the agent
    result = await Runner.run(
        starting_agent=assistant,
        input=history,
    )

    # Update the response message and chat history
    msg.content = result.final_output
    await msg.update()
    cl.user_session.set("chat_history", result.to_input_list())
    print(result.final_output)  # Log the final output for debugging

# Entry point of the application
if __name__ == "__main__":
    asyncio.run(start())

