# Boilerplate Setup

1. Initialize project with uv package manager.

`uv init shellserver`

`cd shellserver`

2. Create virtual environment with uv.

`uv venv`

`source .venv/bin/activate`

3. Install dependencies (MCP[CLI]).

`uv add "mcp[cli]"`

- mcp[cli] should now appear in the pyproject.toml file.

`touch server.py`

`rm main.py`


4. Index Official MCP documentation with Cursor.

`cursor .`

Cursor > Settings > Indexing & Docs > Add Docs

Add url for MPC website:

https://modelcontextprotocol.io



5. Update project with Cursor rules.

Give Cursor the persona of someone who knows Python really well.

This text will be attached to every request we send to Cursor for this project.

Create:

.cursor/rules/python.mdc

'.mdc' tells cursor to recognize file as rules.

Get the file from cursor.directory website, copy contents into python.mdc file.




Prompt:

I want you to implement a simple MCP server from @MCP.  Use the @MCPPythonSDK.  The server should expose one tool which is called the terminal tool which will allow the user to run terminal commands.  Make it simple.

I want you to implement a simple MCP server from @MCP.  Use the @MCPPythonSDK.  The server should expose one tool which is called the terminal tool which will allow the user to run terminal commands.  Make it simple.


Request ID: c14af7bc-f6f8-4a22-a9b4-130f3a092370
{"error":"ERROR_UNSPECIFIED","details":{"title":"Cursor Pro Required","detail":"Agent and Edit rely on custom models that cannot be billed to an API key. Please use a Pro or Business subscription and/or disable API keys. Ask should still work.","additionalInfo":{},"buttons":[],"planChoices":[]}}
Cursor
Agent and Edit rely on custom models that cannot be billed to an API key. Please use a Pro or Business subscription and/or disable API keys. Ask should still work.



uv run server.py

uv run server.py 
Traceback (most recent call last):
  File "/Users/blauerbock/workspaces/mcp/shellserver2/server.py", line 26, in <module>
    mcp.start()
    ^^^^^^^^^
AttributeError: 'FastMCP' object has no attribute 'start'
(shellserver2) (base) blauerbock@Johns-MacBook-Pro-2.local /Users/blauerbock/workspaces/mcp/shellserver2 [main]
% 

Change to mcp.run("stdio")

Integrate with Claude desktop (client).

Claude > Settings > Developer > claude_desktop_config.json

Add another MCP server to the json file.

