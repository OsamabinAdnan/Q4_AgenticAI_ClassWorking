from chatbot import myAgent
import chainlit as cl
import asyncio

@cl.on_chat_start
async def chat_start():
    await cl.Message(
        content="Hello! I am Osama bin Adnan's Agent Manager having expertise in Web Development, Mobile App Development, and Marketing. How can I assist you today?"
    ).send()

@cl.on_message
async def main(message:cl.Message):
    user_input = message.content
    response = asyncio.run(myAgent(user_input))
    await cl.Message(
        content=f"{response}"
    ).send()

