import sys
from agents.researcher import research
from agents.critiquer import critique


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"your question\"")
        sys.exit(1)

    question = sys.argv[1]

    research_output = research(question)
    critique_output = critique(question, research_output)

    print("=== RESEARCH ===")
    print(research_output)
    print("\n=== CRITIQUE ===")
    print(critique_output)


if __name__ == "__main__":
    main()
