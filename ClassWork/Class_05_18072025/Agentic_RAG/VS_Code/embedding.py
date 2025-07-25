# How to create vector Database
# Go to Open AI Platform -> Dashboard -> storage -> vector stores -> 
# create db -> add files -> upload your file -> attach -> copy vector store id and save it

import asyncio
from agents import Agent, Runner, FileSearchTool

agent = Agent(
    name="Assistant",
    instructions= """
    You are acting as me, the owner of this service. 
    Always speak in the first person, as if you are the person providing the service. 
    Be friendly, concise, and helpful. Clearly explain what I offer, answer questions, 
    and keep the conversation natural and tailored to the user's needs. 
    Ask clarifying questions if needed to better assist them.
    """,
    tools=[
        FileSearchTool(
            max_num_results= 3, # Maximum number of results to return
            vector_store_id="your_vector_store_id",  # Replace with your actual vector store ID
        )
    ]
)

async def main():
    result = Runner.run(
        agent,
        input="What services do you offer? Can you help me with my project?",
    )
    print(result.final_output)


asyncio.run(main())