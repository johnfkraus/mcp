import asyncio

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

try:
    load_dotenv()
except Exception as e:
    print(repr(e))  # type: ignore



llm = ChatOpenAI()


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    "/Users/blauerbock/workspaces/mcp/mcp-crash-course-project-sse/servers/math_server.py"
                ],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            },
        }
    )
    try:
        tools = await client.get_tools()
    except Exception as e:
        print(repr(e))  # type: ignore
        return
    
    try:
        agent = create_react_agent(llm, tools)
    except Exception as e:
        print(repr(e))  # type: ignore

    

    result = await agent.ainvoke({"messages": "What is 2 + 2?"})
    # result = await agent.ainvoke(
    #     {"messages": "What is the weather in San Francisco?"}
    # )

    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
