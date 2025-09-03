What is langgraph memory?

LangGraph memory refers to the persistence and state management capabilities in LangGraph, a framework for building stateful, multi-agent applications with Large Language Models (LLMs).

In LangGraph, memory serves several key purposes:

1. **Conversation Memory**: Stores the history of interactions between agents and users, allowing the system to maintain context across multiple conversation turns.

2. **State Persistence**: Maintains the state of your graph/workflow between executions. This includes:
   - Current position in the workflow
   - Variables and data accumulated during execution
   - Decision history and paths taken

3. **Checkpointing**: LangGraph can save snapshots of the entire graph state at various points, enabling:
   - Resume capability if execution is interrupted
   - Time-travel debugging to inspect past states
   - Branching to explore different execution paths

4. **Memory Stores**: LangGraph supports different backend storage options:
   - In-memory storage (for development/testing)
   - SQLite for local persistence
   - PostgreSQL for production deployments
   - Redis for distributed systems

5. **Thread-based Memory**: Organizes memory by conversation threads, allowing multiple independent conversations to maintain their own state.

The memory system in LangGraph is particularly useful for building complex applications like:
- Multi-step workflows that need to remember previous decisions
- Conversational agents that maintain context
- Systems that need to pause and resume processing
- Applications requiring audit trails of decision-making

Memory in LangGraph is implemented through its state management system, where you define the state schema and LangGraph handles the persistence and retrieval automatically as your graph executes.


Repeat, but with MCP server:

What is langgraph memory?

free plan Claude hit the maximum length for this conversation.  Please start a new conversation..

... purchased subscription...

LangGraph memory allows you to store and retrieve information across different steps or iterations of your AI workflow. It's a key feature of LangGraph, a framework for building stateful, multi-step AI applications using LangChain.

Let me explore the documentation to give you more specific details about LangGraph memory.

Now let me fetch the LangGraph documentation:

Now I'll fetch specific information about memory in LangGraph:

Based on the documentation I've reviewed, I can provide you with a comprehensive explanation of LangGraph memory:

# LangGraph Memory

LangGraph memory is a system that allows AI applications to remember information across multiple interactions. It's a critical feature that enables agents to maintain context, learn from feedback, and provide personalized experiences.

## Types of Memory in LangGraph

LangGraph supports two main types of memory:

### 1. Short-Term Memory (Thread-Scoped)

Short-term memory tracks the ongoing conversation within a single session or thread:

- It's implemented as part of the agent's state
- Persisted via thread-scoped checkpoints
- Typically includes conversation history and other stateful data (uploaded files, retrieved documents, generated artifacts)
- Enables multi-turn conversations where the agent remembers previous exchanges

```python
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph

# Create a checkpointer for short-term memory
checkpointer = InMemorySaver()

# Build and compile your graph with the checkpointer
builder = StateGraph(...)
graph = builder.compile(checkpointer=checkpointer)

# Invoke with thread_id to maintain conversation state
graph.invoke(
    {"messages": [{"role": "user", "content": "hi! i am Bob"}]},
    {"configurable": {"thread_id": "1"}},
)
```

### 2. Long-Term Memory (Cross-Thread)

Long-term memory stores information that persists across different sessions or threads:

- Stored in a separate store, not tied to a specific thread
- Organized in custom namespaces and keys (similar to folders and files)
- Can be retrieved at any time in any thread
- Useful for user-specific or application-level data

```python
from langgraph.store.memory import InMemoryStore
from langgraph.graph import StateGraph

# Create a store for long-term memory
store = InMemoryStore()

# Build and compile your graph with the store
builder = StateGraph(...)
graph = builder.compile(store=store)

# Store data in the memory store
store.put(
    ("user_123", "preferences"),  # namespace
    "language",                   # key
    {"preferred_language": "English"}  # value
)
```

## Memory Management Techniques

### Managing Short-Term Memory

To prevent exceeding the LLM's context window limits with long conversations, LangGraph provides several strategies:

1. **Trimming Messages**: Remove the first or last N messages before calling the LLM

```python
from langchain_core.messages.utils import trim_messages, count_tokens_approximately

def call_model(state):
    messages = trim_messages(
        state["messages"],
        strategy="last",
        token_counter=count_tokens_approximately,
        max_tokens=128
    )
    response = model.invoke(messages)
    return {"messages": [response]}
```

2. **Deleting Messages**: Permanently remove specific messages from state

```python
from langchain_core.messages import RemoveMessage

def delete_messages(state):
    messages = state["messages"]
    if len(messages) > 2:
        # remove the earliest two messages
        return {"messages": [RemoveMessage(id=m.id) for m in messages[:2]]}
```

3. **Summarizing Messages**: Replace earlier messages with a summary

```python
from langmem.short_term import SummarizationNode

summarization_node = SummarizationNode(
    token_counter=count_tokens_approximately,
    model=model,
    max_tokens=384,
    max_summary_tokens=128
)
```

### Managing Long-Term Memory

Long-term memory in LangGraph is organized into different types:

1. **Semantic Memory**: Stores facts and knowledge, like user preferences
2. **Episodic Memory**: Records experiences and past actions
3. **Procedural Memory**: Contains instructions or rules for performing tasks

You can write to long-term memory in two ways:
- **In the hot path**: During runtime (real-time updates but impacts latency)
- **In the background**: As a separate background task (no latency impact but potential delays in availability)

## Using Memory in Tools

LangGraph allows agents to access and modify memory through tools:

### Reading Short-Term Memory in Tools

```python
from typing import Annotated
from langgraph.prebuilt import InjectedState, create_react_agent

def get_user_info(
    state: Annotated[CustomState, InjectedState]
) -> str:
    """Look up user info."""
    user_id = state["user_id"]
    return "User is John Smith" if user_id == "user_123" else "Unknown user"
```

### Writing Short-Term Memory from Tools

```python
from langgraph.types import Command

def update_user_info(
    tool_call_id: Annotated[str, InjectedToolCallId],
    config: RunnableConfig
) -> Command:
    """Update user info."""
    user_id = config["configurable"].get("user_id")
    name = "John Smith" if user_id == "user_123" else "Unknown user"
    return Command(update={
        "user_name": name,
        "messages": [ToolMessage("Successfully updated user info", tool_call_id=tool_call_id)]
    })
```

### Reading Long-Term Memory in Tools

```python
from langgraph.config import get_store

def get_user_info(config: RunnableConfig) -> str:
    """Look up user info."""
    store = get_store()
    user_id = config["configurable"].get("user_id")
    user_info = store.get(("users",), user_id)
    return str(user_info.value) if user_info else "Unknown user"
```

### Semantic Search in Long-Term Memory

LangGraph also supports semantic search in memory stores:

```python
from langchain.embeddings import init_embeddings

embeddings = init_embeddings("openai:text-embedding-3-small")
store = InMemoryStore(
    index={
        "embed": embeddings,
        "dims": 1536,
    }
)

# Later, search by semantic similarity
items = store.search(
    ("user_123", "memories"), query="I'm hungry", limit=1
)
```

## Production Considerations

For production, use database-backed storage instead of in-memory solutions:

- PostgreSQL: `PostgresSaver` and `PostgresStore`
- MongoDB: `MongoDBSaver`
- Redis: `RedisSaver` and `RedisStore`

These options provide persistence and scalability for both short-term and long-term memory in production environments.

LangGraph memory is an essential component for building sophisticated AI applications that can maintain context over time, remember user preferences, and deliver personalized experiences across multiple interactions.