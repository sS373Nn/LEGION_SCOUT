from core.client import query

SYSTEM_PROMPT = (
    "You are a research agent. Your job is to thoroughly research and answer the question below. "
    "Be comprehensive and accurate. Show your reasoning."
)


def research(question: str) -> str:
    prompt = f"{SYSTEM_PROMPT}\n\nQuestion: {question}"
    return query(prompt)
