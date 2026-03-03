from unittest.mock import patch
from agents.critiquer import critique


def test_critique_returns_string():
    with patch('agents.critiquer.query', return_value="This research is flawed because..."):
        result = critique("What is the speed of light?", "Light travels at 299,792 km/s.")
        assert isinstance(result, str)


def test_critique_returns_nonempty_string():
    with patch('agents.critiquer.query', return_value="This research is flawed because..."):
        result = critique("What is the speed of light?", "Light travels at 299,792 km/s.")
        assert len(result) > 0


def test_critique_calls_query_once():
    with patch('agents.critiquer.query', return_value="This research is flawed because...") as mock_query:
        critique("What is the speed of light?", "Light travels at 299,792 km/s.")
        mock_query.assert_called_once()


def test_critique_includes_question_in_prompt():
    question = "What is the speed of light?"
    with patch('agents.critiquer.query', return_value="This research is flawed because...") as mock_query:
        critique(question, "Light travels at 299,792 km/s.")
        prompt_used = mock_query.call_args[0][0]
        assert question in prompt_used


def test_critique_includes_research_in_prompt():
    research_output = "Light travels at 299,792 km/s."
    with patch('agents.critiquer.query', return_value="This research is flawed because...") as mock_query:
        critique("What is the speed of light?", research_output)
        prompt_used = mock_query.call_args[0][0]
        assert research_output in prompt_used
