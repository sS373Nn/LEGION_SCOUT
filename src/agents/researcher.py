from core.client import query
from tools.search import search

SYSTEM_PROMPT = (
    "You are a research agent. Your job is to thoroughly research and answer the question below. "
    "Be comprehensive and accurate. Show your reasoning."
)


def research(question: str) -> str:
    results = search(question)
    search_context = "\n\n".join(
        f"[{r['title']}]({r['url']})\n{r['snippet']}" for r in results
    )
    prompt = f"{SYSTEM_PROMPT}\n\nSearch Results:\n{search_context}\n\nQuestion: {question}"
    return query(prompt)
