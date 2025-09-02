
Cursor subscription required, apparently.  $20/month, starting 9/2/25.


I'll implement a simple MCP server with a terminal tool. Let me read the necessary files first to understand the structure.

[4 tools called]

Let me search for additional context about the MCP SDK.

[2 tools called]

Now I'll implement the simple MCP server with a terminal tool. I'll write the code to the server.py file:

[1 tool called]

Now I'll update the README.md file to provide instructions on how to use the server:

[1 tool called]

Let's check for any linting errors in our server.py file:

[1 tool called]

Great! I've implemented a simple MCP server with a terminal tool. Here's what I did:

1. Created a `server.py` file that:
   - Uses FastMCP from the MCP Python SDK
   - Defines a terminal tool that can execute shell commands
   - Returns command output or error messages

2. Updated the README.md with:
   - Installation instructions
   - Usage instructions for both development and Claude Desktop
   - Security warnings about executing terminal commands

To run the server in development mode, you can use:
```bash
mcp dev server.py
```

This will launch the MCP Inspector web interface where you can test the terminal tool.

To install it for use with Claude Desktop:
```bash
mcp install server.py
```

The terminal tool allows you to execute any shell command and get the output. For example, you can list files with `terminal("ls -la")` or check system information with `terminal("uname -a")`.