# LEGION_SCOUT

A research and critique agent pair built to explore agentic coordination patterns.

## What it does

The user submits a question via the CLI. A researcher agent answers it thoroughly, then a critiquer agent tears that answer apart — identifying gaps, logical errors, unsupported claims, and anything the researcher missed or glossed over. Both outputs are printed to the terminal.

The goal is honest analysis, not validation.

## Usage

```bash
cd src
python3 main.py "your question here"
```

## Architecture

Two agents, running sequentially:

1. **Researcher** — given the question, produces a comprehensive answer
2. **Critiquer** — given the original question AND the researcher's output, finds what's wrong with it

The critiquer sees both to catch the most important failure mode: the researcher answering the wrong question entirely.

## A note on the API approach

This project uses the Claude Code CLI (`claude -p`) via subprocess rather than the Anthropic Python SDK. This is an intentional tradeoff.

The SDK requires a separate API key and pay-per-token billing on top of an existing Claude subscription. Since Claude Code is already authenticated against that subscription, we shell out to it directly to avoid paying twice for the same underlying service.

The tradeoff is real: each agent call spawns a new Node.js process, which adds overhead compared to a direct HTTP call via the SDK. For a personal tool where responses are measured in seconds anyway, this is negligible. For a production application or high-volume use, the SDK would be the right call.

If you want to swap to the SDK later, the change is isolated to `src/core/client.py`.

#NOTE#
This does NOT subvert or avoid paying Anthropic in any way. This requires a PAID subscription to Claude Code to work, but avoids the API pay-per-token usually associated with programs such as this. I'm a broke college grad. I can't afford an API on top of a Claude Subscription.

## Running tests

Unit tests only (fast, no CLI calls):
```bash
pytest -m "not integration"
```

Integration tests (hits the real Claude CLI, slow):
```bash
pytest -m integration
```

All tests:
```bash
pytest
```

## Project structure

```
Legion_Scout/
├── pytest.ini               # Test configuration and custom markers
├── requirements.txt
└── src/
    ├── main.py              # CLI entry point
    ├── agents/
    │   ├── researcher.py    # Research agent
    │   └── critiquer.py     # Critique agent
    ├── core/
    │   └── client.py        # Subprocess wrapper for Claude CLI
    └── tests/
        ├── test_researcher.py
        ├── test_critiquer.py
        └── test_integration.py
```

## Dependencies

```
pytest
pytest-mock
```

Requires Claude Code to be installed and authenticated.

**Platform:** Designed to run in Linux or WSL. Running directly in Windows is untested and will likely fail due to how the Claude CLI is invoked via subprocess.
