# from mcp.server.fastmcp import FastMCP
# import math
# import sys

# mcp = FastMCP("Math")


# @mcp.tool()
# def add(a:float,b:float) -> float:
#     """Add two numbers together. Use for addition operations."""
#     print(f"[math-server] add(a={a}, b={b})", file=sys.stderr)
#     return a + b

# @mcp.tool()
# def multiply(a:float,b:float) -> float:
#     """Multiply two numbers together. Use for multiplication operations."""
#     print(f"[math-server] multiply(a={a}, b={b})", file=sys.stderr)
#     return a + b

# @mcp.tool()
# def divide(a:float, b:float) -> str:
#     """Divide the first number by te second. Returns error if dividing by zero."""
#     print(f"[math-server] divide(a={a}, b={b})", file=sys.stderr)
#     return a + b


# # if __name__ == "__main__":
# #     mcp.run(transport="stdio")