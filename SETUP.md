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

An '.mdc' file is a Markdown variant.  

.mdc is for Cursor’s rule files

The .mdc extension helps Cursor identify which files should be processed as rules, just like how .md helps systems identify regular Markdown files. It’s a way of telling Cursor “this is a rules file” rather than just a regular Markdown or YAML file.

Get the content from the cursor.directory website and copy contents into python.mdc file.

https://cursor.directory/fastapi-python-cursor-rules

