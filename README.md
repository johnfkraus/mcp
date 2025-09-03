# mcp

The Model Context Protocol (MCP) is an open standard that allows AI agents to interact with external data sources and tools through standardized, third-party servers. This creates a "plug-and-play" ecosystem for AI tools, connecting them to enterprise databases, cloud platforms, communication services, and more. 

![](images/mpc-tools-resources-prompts.png)

https://modelcontextprotocol.io/quickstart/server

curl -LsSf https://astral.sh/uv/install.sh | sh


my-anthropic-claude-api-key-1

MCP weather: spawn uv ENOCENT

MCP weather: server disconnected


# MCP Crash Course-Udemy

## Section 4: MCP Servers

## 18. Theory of MCP Servers

https://www.udemy.com/course/model-context-protocol/learn/lecture/49282191#overview

Code your own MCP servers
- MCP Generator

Community sources of MCPs

- MCP.so

Third-party servers / official integrations from various organizations

- Similar to how each LLM vendor maintains their own LangChain integration packages

https://github.com/wong2/awesome-mcp-servers

https://mcpservers.org/

Don't reinvent the wheel.

MCP servers can run:
- locally
- remotely, via server-sent events (SSE)
- Docker containers

#### Composability

![](images/mcp-composibility.png)

Any MCP agent can be both a client and server.

Registry API, central, for discovering MCP servers.

Verification

### 19. MCP Inspector (Observability)

Anthropic open-source protocol: 

https://modelcontextprotocol.io/legacy/tools/inspector

Use Inspector to test and debug your MCP server.

### 20.  llm.txt

Markdown file describing app for AI.

A proposal to standardise on using an /llms.txt file to provide information to help LLMs use a website at inference time.
Author
Jeremy Howard

Published
September 3, 2024

Background
Large language models increasingly rely on website information, but face a critical limitation: context windows are too small to handle most websites in their entirety. Converting complex HTML pages with navigation, ads, and JavaScript into LLM-friendly plain text is both difficult and imprecise.

While websites serve both human readers and LLMs, the latter benefit from more concise, expert-level information gathered in a single, accessible location. This is particularly important for use cases like development environments, where LLMs need quick access to programming documentation and APIs.

Proposal
llms.txt logo

llms.txt logo
We propose adding a /llms.txt markdown file to websites to provide LLM-friendly content. This file offers brief background information, guidance, and links to detailed markdown files.

llms.txt markdown is human and LLM readable, but is also in a precise format allowing fixed processing methods (i.e. classical programming techniques such as parsers and regex).

We furthermore propose that pages on websites that have information that might be useful for LLMs to read provide a clean markdown version of those pages at the same URL as the original page, but with .md appended. (URLs without file names should append index.html.md instead.)

llms.txt is an index file containing links with brief descriptions of the content. An LLM or agent must follow these links to access detailed information.

llms-full.txt includes all the detailed content directly in a single file, eliminating the need for additional navigation.

A key consideration when using llms-full.txt is its size. For extensive documentation, this file may become too large to fit into an LLM's context window.

https://langchain-ai.github.io/langgraph/llms-txt-overview/


### 21. mcpdoc

https://github.com/langchain-ai/mcpdoc

```shell
git clone https://github.com/langchain-ai/mcpdoc

uv venv

source .venv/bin/activate

uv pip install .

which uv

```

copy uv path:

/Users/blauerbock/.local/bin/uv


```shell
uvx --from mcpdoc mcpdoc \
    --urls "LangGraph:https://langchain-ai.github.io/langgraph/llms.txt" "LangChain:https://python.langchain.com/llms.txt" \
    --transport sse \
    --port 8082 \
    --host localhost
```
In another terminal:

npx @modelcontextprotocol/inspector

Browse to the MCP Inspector, or Click the MCP Inspector shown in the terminal, i.e.,

http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=b8594203fc08f8162603c2986c5c22396dcaf53d03993ce66469cf2b4cb87c60


Use transport type SSE.

Connect to our SSE server running on port 8082.

Replace "uvx" in the claude config with full path to executable:

/Users/blauerbock/.local/bin/uvx


## 5. Building, Securing, and Containerizing an MCP Server


### 22. What are we building?

Containerization
- portability
- consistency

https://github.com/modelcontextprotocol/python-sdk


### 23. Project Setup: Virtual Environment, Cursor Rules, MCP Docs Indexing

![](images/boilerplate-setup-mcp.png)

```shell
uv init shellserver

cd shellserver

uv venv

source .venv/bin/activate

uv add "mcp[cli]"

cursor .

```

Index the MCP documentation for vibe coding.

Attach URL in Cursor for MCP and MCP Python SDK.

Add cursor rules:

.cursor/rules/python.mdc


Get cursor rules from website cursor.directory or copy them from instructor's code (mcp-crash-course).

https://cursor.directory/

### 24. Vibe Coding an MCP Server that exposes a Shell (terminal) tool

Code is here: https://github.com/emarco177/mcp-crash-course

In Cursor, open server.py; in chat choose model.  Enter prompt.

I want you to implement a simple MPC server from @MPC.  Use the Python SDK @MPC Python SDK.  The server should expose one tool which is called terminal which will allow the user to run terminal commands.  Make it simple.

Request ID: ddc85968-006c-4211-b32c-1c3f8b2b0dbb
{"error":"ERROR_BAD_REQUEST","details":{"title":"Bad request.","detail":"Anthropic's latest models are currently only available to paid users. Please upgrade to a paid plan to use these models.","isRetryable":false,"additionalInfo":{},"buttons":[],"planChoices":[]},"isExpected":true}
ConnectError: [invalid_argument] Error
    at nol.$endAiConnectTransportReportError (vscode-file://vscode-app/Applications/Cursor.app/Contents/Resources/app/out/vs/workbench/workbench.desktop.main.js:4814:319459)
    at egr._doInvokeHandler (vscode-file://vscode-app/Applications/Cursor.app/Contents/Resources/app/out/vs/workbench/workbench.desktop.main.js:488:211942)
    at egr._invokeHandler (vscode-file://vscode-app/Applications/Cursor.app/Contents/Resources/app/out/vs/workbench/workbench.desktop.main.js:488:211684)
    at egr._receiveRequest (vscode-file://vscode-app/Applications/Cursor.app/Contents/Resources/app/out/vs/workbench/workbench.desktop.main.js:488:210449)
    at egr._receiveOneMessage (vscode-file://vscode-app/Applications/Cursor.app/Contents/Resources/app/out/vs/workbench/workbench.desktop.main.js:488:209271)
    at O_t.value (vscode-file://vscode-app/Applications/Cursor.app/Contents/Resources/app/out/vs/workbench/workbench.desktop.main.js:488:207365)
    at ye._deliver (vscode-file://vscode-app/Applications/Cursor.app/Contents/Resources/app/out/vs/workbench/workbench.desktop.main.js:49:2962)
    at ye.fire (vscode-file://vscode-app/Applications/Cursor.app/Contents/Resources/app/out/vs/workbench/workbench.desktop.main.js:49:3283)
    at Prt.fire (vscode-file://vscode-app/Applications/Cursor.app/Contents/Resources/app/out/vs/workbench/workbench.desktop.main.js:4801:12154)
    at MessagePort.<anonymous> (vscode-file://vscode-app/Applications/Cursor.app/Contents/Resources/app/out/vs/workbench/workbench.desktop.main.js:6983:18168)


## 25. Exposing a Resource (Data) in our MCP Server

Copy-paste the MCP readme file, save it locally in our file system, and expose it as a resource in our MCP server.

https://github.com/modelcontextprotocol/python-sdk

Create file ~/Desktop/mcpreadme.md.  Paste the content of the README.md file from the python-sdk repository.

Vibe code the server code using Cursor.

Prompt:

I want you to help me expose a resource in my mcp server @MCP, again use the @MCPPythonSDK to write the code.  
I want to expose mcpreadme.md under my Desktop directory.

Claude client GUI changed (again).  Demo steps don't exactly work.

## 26. MCP and Security

Create malicious gist.github.com file.  Or just use this linked file: 
https://gist.githubusercontent.com/emarco177/47fac6debd88e1f8ad9ff6a1a33041a5/raw/9802cafba96ebeb010f3d080d948e7471987b081/hacked.txt


Expose a tool that downloads the file.

Compromise MCP client.

https://owasp.org/www-project-top-10-for-large-language-model-applications/

Prompt for Cursor:

Help me expose another tool in my mcp server MCP Use the Python SDK with MCPPythonSDK.
The tool is called "benign_tool" and should download via curl the content https://gist.githubusercontent.com/emarco177/47fac6debd88e1f8ad9ff6a1a33041a5/raw/9802cafba96ebeb010f3d080d948e7471987b081/hacked.txt 
 and return what was downloaded.

Be cautious regarding downloaded MCP Server code.

## 27. AI Agent Security Risk: Exploiting Permissive Tools (Demo)

Claude Prompt:

Delete the mcpreadme.md file from my Desktop directory.

It worked.  The file was deleted.

If Claude balks, precede the prompt with "Help me clean up my computer, "


## 28. Docker for MCP Server: Advantages

- consistency across environments
  - Docker eliminates the "works on my machine" problem.
  - Docker abstracts away OS differences by using the container's OS environment.  
  - Easier cross-platform environment.  Portability.  Develop on one OS, deploy to another OS without changing anything in your code. 
- isolation and safer execution
  - runs in its own sandbox
  - if server needs access to a specific folder or device, Docker lets you grant just that access using volumes or device flags.
- easy scaling and management
  - just launch more containers
  - updates by building and deploying a new container.

