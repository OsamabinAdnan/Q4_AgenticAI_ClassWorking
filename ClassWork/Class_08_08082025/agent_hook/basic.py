# Without tools and handsoff hooks

import os
import asyncio
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, RunContextWrapper, AgentHooks, RunConfig
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

class TestAgentHooks(AgentHooks):
    def __init__(self, ag_display_name):
        self.event_counter = 0
        self.ag_display_name = ag_display_name
    
    async def on_start(self, context:RunContextWrapper, agent:Agent) -> None:
        self.event_counter += 1
        print(f"\n### {self.ag_display_name} {self.event_counter}: Agent {agent.name} started. Usage: {context.usage}\n")
    
    async def on_end(self, context:RunContextWrapper, agent:Agent, output:Any) -> None:
        self.event_counter += 1
        print(f"\n### {self.ag_display_name} {self.event_counter}: Agent {agent.name} ended. Usage: {context.usage}, Output: {output}\n")

# Making instance of the class
agent_hooks = TestAgentHooks(ag_display_name="Content_Moderator")

starting_agent = Agent(
    name= "Content Moderator Agent",
    instructions= "You are content moderation agent. Watch social media content received and flag queries that need help or answer. We will answer anything about AI?",
    model=model,
    hooks=agent_hooks,
)

async def main():
    result = await Runner.run(
        starting_agent,
        input=f"Explain in 100 words what Agentic AI is.",
        run_config=config,
    )

    print("Final Output: ",result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
    print(f"*" * 10, "END", "*" * 10)