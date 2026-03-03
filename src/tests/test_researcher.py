from unittest.mock import patch
from agents.researcher import research


def test_research_returns_string():
    with patch('agents.researcher.query', return_value="Some research output."):
        result = research("What is the speed of light?")
        assert isinstance(result, str)


def test_research_returns_nonempty_string():
    with patch('agents.researcher.query', return_value="Some research output."):
        result = research("What is the speed of light?")
        assert len(result) > 0


def test_research_calls_query_once():
    with patch('agents.researcher.query', return_value="Some research output.") as mock_query:
        research("What is the speed of light?")
        mock_query.assert_called_once()


def test_research_includes_question_in_prompt():
    question = "What is the speed of light?"
    with patch('agents.researcher.query', return_value="Some research output.") as mock_query:
        research(question)
        prompt_used = mock_query.call_args[0][0]
        assert question in prompt_used
