import subprocess
import shlex
from typing import Optional
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

# Initialize the MCP server
mcp = FastMCP("TerminalServer")

class TerminalInput(BaseModel):
    """Input model for the terminal tool."""
    command: str = Field(..., description="The terminal command to execute")
    timeout: Optional[int] = Field(60, description="Timeout in seconds for the command execution")

class TerminalOutput(BaseModel):
    """Output model for the terminal tool."""
    stdout: str = Field("", description="Standard output from the command")
    stderr: str = Field("", description="Standard error from the command")
    exit_code: int = Field(0, description="Exit code from the command")
    success: bool = Field(True, description="Whether the command executed successfully")

@mcp.tool()
def terminal(params: TerminalInput) -> TerminalOutput:
    """
    Execute a terminal command and return its output.
    
    This tool allows running shell commands and returns the stdout, stderr, and exit code.
    """
    try:
        # Run the command with timeout
        process = subprocess.run(
            params.command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=params.timeout,
            check=False  # Don't raise an exception on non-zero exit code
        )
        
        return TerminalOutput(
            stdout=process.stdout,
            stderr=process.stderr,
            exit_code=process.returncode,
            success=process.returncode == 0
        )
    except subprocess.TimeoutExpired:
        return TerminalOutput(
            stdout="",
            stderr=f"Command timed out after {params.timeout} seconds",
            exit_code=124,  # Standard timeout exit code
            success=False
        )
    except Exception as e:
        return TerminalOutput(
            stdout="",
            stderr=f"Error executing command: {str(e)}",
            exit_code=1,
            success=False
        )

if __name__ == "__main__":
    # Run the MCP server
    mcp.run(transport="stdio")