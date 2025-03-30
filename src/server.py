from fastmcp import FastMCP

mcp = FastMCP("rubber-duck")

@mcp.tool()
def rubber_duck(message: str) -> str:
    """A rubber duck that listens but doesn't respond"""
    return ""

@mcp.tool()
def squeak(message: str) -> str:
    """A squeaky rubber duck that squeaks when you squeeze it"""
    return "Squeak!"



