from mcp.server.fastmcp import FastMCP
from utils.arxiv import arxiv_search

mcp = FastMCP("arxiv-tool")

@mcp.tool()
def search_arxiv(query: str, max_results: int = 10) -> list:
    return arxiv_search(query, max_results)

if __name__ == "__main__":
    mcp.run()