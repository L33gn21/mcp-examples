from mcp.server.fastmcp import FastMCP

mcp = FastMCP("testMCP")

@mcp.tool()
def decrypt_text(text: str) -> str:
    """decrypt text.""" 
    if(text == "qewioqiwdnowddq"): 
        return "crack wow!!!!!"
    raise Exception("I dont know...") 




if __name__ == "__main__": 
    print("Starting MCP server...")
    mcp.run()