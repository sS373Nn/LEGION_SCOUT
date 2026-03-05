import os


def search(query: str) -> list[dict]:
    provider = os.environ.get("SEARCH_PROVIDER", "tavily")
    if provider == "tavily":
        from tools.tavily import search as _search
        return _search(query)
    raise ValueError(f"Unknown search provider: {provider}")
