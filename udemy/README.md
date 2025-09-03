# MCP crash course - Udemy

https://modelcontextprotocol.io/introduction

Course Discord Server

https://discord.gg/SP2cz4JcGg

https://docs.cursor.com/context/model-context-protocol

https://github.com/modelcontextprotocol/quickstart-resources


https://github.com/emarco177/mcp-crash-course



{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather",
        "run",
        "weather.py"
      ]
    }
  }
}


{
  "mcpServers": {
    "weather": {
      "command": "node",
      "args": ["/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather/build/index.js"]
    }
  }
}



Core MCP Concepts
https://modelcontextprotocol.io/quickstart/server#weather-api-helper-functions


MCP servers can provide three main types of capabilities:
- Resources: File-like data that can be read by clients (like API responses or file contents)
- Tools: Functions that can be called by the LLM (with user approval)
- Prompts: Pre-written templates that help users accomplish specific tasks
