
import asyncio

from agents import Agent, ModelSettings, trace, Runner
from agents.mcp import MCPServerStdio
from dotenv import load_dotenv

load_dotenv()


async def main():
    async with MCPServerStdio(
            params={
                "command": "uvx",
                "args": ["python-interpreter-mcp"],
            }
    ) as server:
        with trace(workflow_name="PyScript running agent"):
            agent = Agent(
                name="Script Executor",
                instructions="Generate python code and execute with tools. Always use print statements "
                             "to get outputs from functions and follow PEP-8. If user asks for function, write"
                             "unittest under the function before passing it. Iterate until the test passes and return the function."
                             "Strictly follow instructions",
                model="gpt-4o-mini",
                model_settings=ModelSettings(max_tokens=400),
                mcp_servers=[server],
            )
            message = "Write a python function to generate n fibonacci numbers."
            result = await Runner.run(agent, message)

            print(result.final_output)

if __name__ == '__main__':
    asyncio.run(main())
