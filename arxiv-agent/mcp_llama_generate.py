from mcp.server.fastmcp import FastMCP
from utils.llama import llama_generate

mcp = FastMCP("llm-tool")

@mcp.tool()
def generate(prompt: str, max_tokens: int = 1500) -> str:
    return llama_generate(prompt, max_tokens)

if __name__ == "__main__":
    mcp.run()


