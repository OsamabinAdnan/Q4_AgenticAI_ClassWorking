import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool
import asyncio
import chainlit as cl

load_dotenv()

set_tracing_disabled(True)  # Disable tracing for the agent

@function_tool
def get_weather(city: str) -> str:
    """
    Get the current weather for a given city.
    """
    # This is a placeholder implementation. Replace with actual weather API call.
    return f"The current weather in {city} is sunny with a temperature of 25°C."

@cl.on_chat_start
async def start():
    MODEL="gemini-2.0-flash"
    API_KEY = os.getenv("GEMINI_API_KEY")

    if not API_KEY:
        raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
    
    external_client = AsyncOpenAI(
        api_key=API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    model = OpenAIChatCompletionsModel(
        model=MODEL,
        openai_client=external_client,
    )

    cl.user_session.set("chat_history", []) # Initialize chat history

    weather_assistant = Agent(
        name="Weather Assistant",
        instructions=f"You are a helpful assistant that provides weather information for cities.",
        model=model,
        tools=[get_weather],  # Register the weather function as a tool
    )

    cl.user_session.set("weather_assistant", weather_assistant) # Store the agent in user session

    await cl.Message(
        content= "Welcome to the Weather Assistant! You can ask me about the weather in any city.",
    ).send()

@cl.on_message
async def main(message:cl.Message):
    msg = await cl.Message(content="Thinking...").send()
    assistant = cl.user_session.get("weather_assistant") # Retrieve the agent from user session
    history = cl.user_session.get("chat_history") or [] # Retrieve chat history

    history.append(
        {
            "role": "user",
            "content": message.content
        }
    )

    result = await Runner.run(
        starting_agent=assistant,
        input=history,
    )

    msg.content = result.final_output
    await msg.update()
    cl.user_session.set("chat_history", result.to_input_list())  # Update chat history
    print(result.final_output)  # Log the final output for debugging

if __name__ == "__main__":
    asyncio.run(start())

