import os
import asyncio
import random
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, ItemHelpers, function_tool
from dotenv import load_dotenv

load_dotenv()

set_tracing_disabled(True)

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set")

@function_tool
def how_many_jokes() -> int:
    return random.randint(1, 10)

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)

async def main():
    agent = Agent(
        name="Joker",
        instructions="First call the `how_many_jokes` function to get the number of jokes to generate. Then generate that many jokes in English language only. Please make sure to generate jokes that are funny.",
        tools=[how_many_jokes],
        model=model,
    )

    result = Runner.run_streamed(
        starting_agent=agent,
        input="Hello"
    )

    print("=== Run Starting ===")

    async for event in result.stream_events():
        # We'll ignore the raw responses event deltas
        if event.type == "raw_response_event":
            continue
        # When the agent updates, print that
        elif event.type == "agent_updated_stream_event":
            print(f"Agent updated: {event.new_agent.name}")
            continue
        # When items are generated, print them
        elif event.type == "run_item_stream_event":
            if event.item.type == "tool_call_item":
                print(f"Tool was called: {event.item.raw_item.name}")
            elif event.item.type == "tool_call_output_item":
                print(f"Tool output: {event.item.output}")
            elif event.item.type == "message_output_item":
                print(f"Message output:\n {ItemHelpers.text_message_output(event.item)}")
            else:
                pass # Ignore other types of events
    
    print("=== Run Complete ===")

if __name__ == "__main__":
    asyncio.run(main())