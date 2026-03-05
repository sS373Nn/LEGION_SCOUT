import os
import pytest
from unittest.mock import patch
from tools.search import search


FAKE_RESULTS = [{"title": "T", "url": "http://example.com", "snippet": "S"}]


def test_dispatches_to_tavily_when_set():
    with patch.dict(os.environ, {"SEARCH_PROVIDER": "tavily"}):
        with patch("tools.tavily.search", return_value=FAKE_RESULTS) as mock:
            result = search("query")
            mock.assert_called_once_with("query")


def test_returns_results_from_provider():
    with patch.dict(os.environ, {"SEARCH_PROVIDER": "tavily"}):
        with patch("tools.tavily.search", return_value=FAKE_RESULTS):
            result = search("query")
            assert result == FAKE_RESULTS


def test_raises_for_unknown_provider():
    with patch.dict(os.environ, {"SEARCH_PROVIDER": "unknown"}):
        with pytest.raises(ValueError):
            search("query")
