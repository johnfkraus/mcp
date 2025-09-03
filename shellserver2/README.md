# Terminal Server MCP

A simple MCP (Model Context Protocol) server that exposes a terminal tool to run shell commands.

## Installation

Make sure you have Python 3.12 or higher installed.

1. Clone this repository
2. Install dependencies:
```bash
uv add "mcp[cli]"
```

## Usage

### Development Mode

Run the server in development mode to test and debug:

```bash
mcp dev server.py
```

This will launch the MCP Inspector web interface where you can interact with the terminal tool.

### Install to Claude Desktop

To use the terminal tool with Claude Desktop:

```bash
mcp install server.py
```

## Tools

The server exposes the following tools:

- **terminal**: Executes a terminal command and returns its output.
- **benign_tool**: Downloads content from a specific URL and returns the downloaded content.
- **get_mcpreadme**: Retrieves the contents of the mcpreadme.md file from the Desktop directory.

### Example Usage

In Claude Desktop or the MCP Inspector:

```
Use the terminal tool to list files in the current directory:
terminal("ls -la")

Use the benign_tool to download content from a URL:
benign_tool()

Retrieve the contents of mcpreadme.md from the Desktop:
get_mcpreadme()
```

## Security Warning

This tool executes terminal commands directly on your system. Use with caution and only in trusted environments.
