import asyncio

from dotenv import load_dotenv

from claude_agent_sdk import (
    query,
    ClaudeAgentOptions,
)

from claude_agent_sdk.types import (
    AssistantMessage,
    ResultMessage,
    TextBlock,
)


async def run_query(question: str):
    options = ClaudeAgentOptions(
        model="claude-haiku-4-5",
    )

    async for message in query(
        prompt=question,
        options=options,
    ):
        print(f"type: {type(message).__name__}")

        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(f"response: {block.text}")

        if isinstance(message, ResultMessage):
            print(f"cost: {message.total_cost_usd}")


async def see_if_tools_work():
    await run_query(
        "Go to directai.blog and find the latest post."
    )


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(see_if_tools_work())