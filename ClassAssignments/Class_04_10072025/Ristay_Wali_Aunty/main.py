import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, function_tool, set_tracing_disabled
from openai import AsyncOpenAI
from whatsapp import send_whatsapp_message
import chainlit as cl

load_dotenv()

set_tracing_disabled(True)

@function_tool
def get_user_data(min_age:int)->list[dict]:
    "Retrieve user data based on minimum age"
    users = [
        {"name": "John Doe", "age": 30},
        {"name": "Jane Smith", "age": 25},
        {"name": "Bob Johnson", "age": 20},
        {"name": "Alice Brown", "age": 27},
        {"name": "Charlie Wilson", "age": 24},
        {"name": "Eva Davis", "age": 22},
        {"name": "David Lee", "age": 19},

    ]

    for user in users:
        if user["age"] <= min_age:
            users.remove(user)
    
    return users

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables")

my_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

my_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=my_client,
)

agent = Agent(
    name="Aunty",
    model=my_model,
    tools=[get_user_data, send_whatsapp_message],
    instructions=
    """
    "You are a warm and wise 'Rishtey Wali Auntie' who helps people/candidates find matches", 
    "You can use the get_user_data function to get details of users based on their age",
    "You can use the send_whatsapp_message function to send a WhatsApp message to the user but first ask user number on which to send the message using send_whatsapp_message function",
    """,
)

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hi Beta! I am your Rishtay Wali Auntie, Ammi ko bhejo ristay ki bat k leay!").send()

@cl.on_message
async def handle_message(message:cl.Message):
    reply = await cl.Message("Processing...").send()
    history = cl.user_session.get("history") or []
    history.append(
        {
            "role": "user",
            "content": message.content,
        }
    )
    
    result = Runner.run_sync(
        starting_agent=agent, 
        input= history
    )

    history.append(
        {
            "role": "assistant",
            "content": result.final_output,
        }
    )

    cl.user_session.set("history", history)

    reply.content = result.final_output
    await reply.update()