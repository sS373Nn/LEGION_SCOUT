import os
from tavily import TavilyClient


def search(query: str) -> list[dict]:
    client = TavilyClient(os.environ["TAVILY_API_KEY"])
    response = client.search(query=query, search_depth="advanced", max_results=3)
    results = response.get("results", [])
    if not results:
        raise RuntimeError(f"Tavily returned no results for query: {query!r}")
    return [
        {"title": r["title"], "url": r["url"], "snippet": r["content"]}
        for r in results
    ]
