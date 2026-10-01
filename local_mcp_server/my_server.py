import random
from fastmcp import FastMCP

# creating a FastMcp server instance
mcp = FastMCP("My mcp server demo")

@mcp.tool
def generate_random_int(min_value: int, max_value: int) -> int:
    """Generate a random integer between min_value and max_value."""
    return random.randint(min_value, max_value)

@mcp.tool
def add_three_numbers(a: int, b: int, c: int) -> int:
    """Add three numbers together"""
    return a + b + c




if __name__ == "__main__":
    mcp.run()    