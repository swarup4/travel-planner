from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def search_tool(query: str):
    """Searches the web and returns results."""
    search = DuckDuckGoSearchResults(num_results=10, verbose=True)
    return search.run(query)