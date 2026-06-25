# calculator_server.py
import sys
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP Server named "CalculatorServer"
mcp = FastMCP("CalculatorServer")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtracts b from a."""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> str:
    """Divides a by b. Handles division by zero errors safely."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return str(a / b)

if __name__ == "__main__":
    # Start the server using the stdio transport layer
    mcp.run(transport="stdio")
