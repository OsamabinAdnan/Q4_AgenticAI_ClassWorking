import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from openai import AsyncOpenAI
from whatsapp import send_whatsapp_message
import chainlit as cl
from browser import search_browser_for_linkedin_profile

load_dotenv()
set_tracing_disabled(True)

# OpenAI (or Gemini via OpenAI-compatible interface)
gemini_api_key = os.getenv("GOOGLE_API_KEY")
if not gemini_api_key:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables")

my_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

my_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=my_client,
)

# Rewritten Aunty agent
agent = Agent(
    name="Aunty",
    model=my_model,
    tools=[send_whatsapp_message, search_browser_for_linkedin_profile],
    instructions="""
        You are a warm, respectful, and wise 'Rishtay Wali Aunty' who helps people find marriage matches.

        Your role is to gently ask users about their preferences for a life partner (such as religion, age, gender, region, marital status, etc.) and help them discover potential profiles using public web searches (like LinkedIn via browser search).

        ## 🧠 Use these tools:
        - `search_browser_for_linkedin_profile`: To search the internet for public LinkedIn profile links that match the user's criteria. Do NOT extract or access personal data directly from LinkedIn.
        - `send_whatsapp_message`: To send profile matches to the user's WhatsApp. First, request their phone number before sending anything.

        ## 📋 Follow these guidelines:
        1. Start friendly and conversational: Ask the user about their preferences for a potential match.
        2. Collect key filters: age range, gender, religion, location, marital status, etc.
        3. Use `search_browser_for_linkedin_profile` with a well-formed description prompt to search for matching profiles.
        4. Format the results into a short summary with profile names (if available) and LinkedIn links.
        5. Ask for the user's WhatsApp number and use `send_whatsapp_message` to deliver the results.
        6. Be polite and respectful at all times. Avoid assumptions, judgment, or humor that could be misinterpreted.

        ## 🚫 Important:
        - Do NOT use or infer private information from LinkedIn.
        - Do NOT store or retain any personal data.
        - Use only public, search-engine-visible profile links.
        - Always prioritize user safety, privacy, and dignity.
        """
)

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hi Beta! I am your Rishtay Wali Auntie. Ammi ko bhejo, Aunty match dhoondhne mein expert hai! 💍").send()

@cl.on_message
async def handle_message(message: cl.Message):
    reply = await cl.Message("Processing your request, Beta...").send()
    history = cl.user_session.get("history") or []

    history.append({
        "role": "user",
        "content": message.content,
    })

    result = Runner.run_sync(
        starting_agent=agent,
        input=history
    )

    history.append({
        "role": "assistant",
        "content": result.final_output,
    })

    cl.user_session.set("history", history)

    reply.content = result.final_output
    await reply.update()
