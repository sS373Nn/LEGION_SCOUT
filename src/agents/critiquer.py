from core.client import query

SYSTEM_PROMPT = (
    "You are a critical analysis agent. Your job is to find flaws. "
    "Do not summarize what the researcher got right. Do not soften your criticism. "
    "Identify gaps, logical errors, unsupported claims, and aspects of the original question that went unanswered. "
    "Assume the user wants brutal honesty, not validation."
)


def critique(question: str, research_output: str) -> str:
    prompt = (
        f"{SYSTEM_PROMPT}\n\n"
        f"Original question: {question}\n\n"
        f"Research to critique:\n{research_output}"
    )
    return query(prompt)
