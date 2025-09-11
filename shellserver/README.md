# MCP Terminal Server

A simple MCP server that exposes a tool to run terminal commands.

## Installation

1. Ensure you have Python 3.11 or higher installed
2. Install the dependencies:

```bash
pip install -e .
```

## Usage

### Starting the Server

Run the server using:

```bash
python server.py
```

### Testing with MCP Inspector

You can test the server using the MCP Inspector:

```bash
mcp dev server.py
```

### Example Usage

The server exposes a single tool called `terminal` that accepts a command string and returns the command output.

Example input:
```json
{
  "command": "ls -la",
  "timeout": 30
}
```

Example output:
```json
{
  "stdout": "total 16\ndrwxr-xr-x  5 user  group  160 Sep 27 10:00 .\ndrwxr-xr-x  8 user  group  256 Sep 27 09:55 ..\n-rw-r--r--  1 user  group  321 Sep 27 10:00 README.md\n-rw-r--r--  1 user  group  160 Sep 27 10:00 server.py\n",
  "stderr": "",
  "exit_code": 0,
  "success": true
}
```

## Security Considerations

This server allows execution of arbitrary terminal commands, which can be dangerous. Use with caution and consider:

1. Running in a restricted environment or container
2. Implementing an allowlist of permitted commands
3. Adding authentication if needed
4. Not using this in production without proper security measures

## License

MIT License
