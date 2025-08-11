import os
import asyncio
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, RunContextWrapper, RunHooks, RunConfig
from openai import AsyncOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Any
from rich import print

load_dotenv()
set_tracing_disabled(True)

BASE_URL="https://generativelanguage.googleapis.com/v1beta/openai/"

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

external_cllient = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url=BASE_URL,
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_cllient,
)

config = RunConfig(
    model=model,
    tracing_disabled=True,
)

class TestHooks(RunHooks):
    def __init__(self):
        self.event_counter = 0
        self.name = "TestHooks"

    async def on_agent_start(self, context: RunContextWrapper, agent: Agent) -> None:
        self.event_counter += 1
        print(f"### {self.name} {self.event_counter}: Agent {agent.name} started. Usage: {context.usage}")

    async def on_agent_end(self, context: RunContextWrapper, agent: Agent, output: Any) -> None:
        self.event_counter += 1
        print(f"### {self.name} {self.event_counter}: Agent {agent.name} ended. Usage: {context.usage}, Output: {output}")

start_hook = TestHooks()

start_agent = Agent(
    name="Content Moderator Agent",
    instructions="You are content moderation agent. Watch social media content received and flag queries that need help or answer. We will answer anything about AI?",
    model=model
)

async def main():
  result = await Runner.run(
      start_agent,
      hooks=start_hook,
      input=f"Will Agentic AI Die at end of 2025?."
  )

  print(result.final_output)

asyncio.run(main())
print("*" * 10,"end", "*" * 10)