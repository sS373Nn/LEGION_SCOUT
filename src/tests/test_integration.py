import pytest
from dotenv import load_dotenv
from agents.researcher import research
from agents.critiquer import critique

load_dotenv()

# Integration tests hit the real Claude CLI. Run explicitly with: pytest -m integration
pytestmark = pytest.mark.integration


@pytest.mark.integration
def test_full_pipeline():
    question = "What are the main causes of the French Revolution?"

    research_output = research(question)
    assert isinstance(research_output, str)
    assert len(research_output) > 0

    critique_output = critique(question, research_output)
    assert isinstance(critique_output, str)
    assert len(critique_output) > 0
