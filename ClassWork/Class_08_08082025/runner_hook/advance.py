import os
import asyncio
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, RunContextWrapper, RunHooks, RunConfig, Usage, Tool, function_tool, set_default_openai_client
from openai import AsyncOpenAI
from dotenv import load_dotenv
from typing import Any
from rich import print
import random

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

set_default_openai_client(external_cllient)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_cllient,
)

config = RunConfig(
    model=model,
    tracing_disabled=True,
)


class ExampleHooks(RunHooks):
    def __init__(self):
        self.event_counter = 0

    def _usage_to_str(self, usage: Usage) -> str:
        return f"{usage.requests} requests, {usage.input_tokens} input tokens, {usage.output_tokens} output tokens, {usage.total_tokens} total tokens"

    async def on_agent_start(self, context: RunContextWrapper, agent: Agent) -> None:
        self.event_counter += 1
        print(
            f"\n### {self.event_counter}: Agent {agent.name} started. Usage: {self._usage_to_str(context.usage)}"
        )

    async def on_agent_end(self, context: RunContextWrapper, agent: Agent, output: Any) -> None:
        self.event_counter += 1
        print(
            f"\n### {self.event_counter}: Agent {agent.name} ended with output {output}. Usage: {self._usage_to_str(context.usage)}"
        )

    async def on_tool_start(self, context: RunContextWrapper, agent: Agent, tool: Tool) -> None:
        self.event_counter += 1
        print(
            f"\n### {self.event_counter}: Tool {tool.name} started. Usage: {self._usage_to_str(context.usage)}"
        )

    async def on_tool_end(
        self, context: RunContextWrapper, agent: Agent, tool: Tool, result: str
    ) -> None:
        self.event_counter += 1
        print(
            f"\n### {self.event_counter}: Tool {tool.name} ended with result {result}. Usage: {self._usage_to_str(context.usage)}"
        )

    async def on_handoff(
        self, context: RunContextWrapper, from_agent: Agent, to_agent: Agent
    ) -> None:
        self.event_counter += 1
        print(
            f"\n### {self.event_counter}: Handoff from {from_agent.name} to {to_agent.name}. Usage: {self._usage_to_str(context.usage)}"
        )

hooks = ExampleHooks()

@function_tool("random_number")
def random_number(max: int) -> int:
    """Generate a random number up to the provided max."""
    return random.randint(0, max)


@function_tool("multiply_by_two")
def multiply_by_two(x: int) -> int:
    """Return x times two."""
    return x * 2


multiply_agent = Agent(
    name="Multiply Agent",
    instructions="Multiply the number by 2 and then return the final result.",
    tools=[multiply_by_two],
    model=model
)

start_agent = Agent(
    name="Start Agent",
    instructions="Generate a random number. If it's even, stop. If it's odd, hand off to the multipler agent.",
    tools=[random_number],
    handoffs=[multiply_agent],
    model=model
)

async def main() -> None:
    user_input = input("Enter a max number: ")
    ans = await Runner.run(
        start_agent,
        hooks=hooks,
        input=f"Generate a random number between 0 and {user_input}.",
    )

    print(ans.final_output)

    print("Done!")

asyncio.run(main())