import os
from tavily import TavilyClient


def search(query: str) -> list[dict]:
    client = TavilyClient(os.environ["TAVILY_API_KEY"])
    response = client.search(query=query, search_depth="advanced")
    return [
        {"title": r["title"], "url": r["url"], "snippet": r["content"]}
        for r in response["results"]
    ]
