from mcp.server.fastmcp import FastMCP
import subprocess

# Initialize the MCP server
mcp = FastMCP("TerminalServer")

@mcp.tool()
def terminal(command: str) -> str:
    """
    Execute a terminal command and return its output.

    Args:
        command (str): The terminal command to execute.

    Returns:
        str: The output of the command.
    """
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

if __name__ == "__main__":
    # Start the server when the script is run directly
    # mcp.start()
    # mcp.run()
    mcp.run("stdio")


