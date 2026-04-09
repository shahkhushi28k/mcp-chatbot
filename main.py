from fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("math-server")

# Example tool
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b

# Run server
if __name__ == "__main__":
    mcp.run()