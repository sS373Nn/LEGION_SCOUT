import os
from unittest.mock import patch
from tools.tavily import search


FAKE_RESPONSE = {
    "results": [
        {"title": "Result 1", "url": "http://example.com/1", "content": "Snippet 1"},
        {"title": "Result 2", "url": "http://example.com/2", "content": "Snippet 2"},
    ]
}


def test_search_returns_list():
    with patch.dict(os.environ, {"TAVILY_API_KEY": "fake-key"}):
        with patch("tools.tavily.TavilyClient") as mock_client:
            mock_client.return_value.search.return_value = FAKE_RESPONSE
            result = search("test query")
            assert isinstance(result, list)


def test_search_result_has_required_keys():
    with patch.dict(os.environ, {"TAVILY_API_KEY": "fake-key"}):
        with patch("tools.tavily.TavilyClient") as mock_client:
            mock_client.return_value.search.return_value = FAKE_RESPONSE
            result = search("test query")
            assert all("title" in r and "url" in r and "snippet" in r for r in result)


def test_search_maps_content_to_snippet():
    with patch.dict(os.environ, {"TAVILY_API_KEY": "fake-key"}):
        with patch("tools.tavily.TavilyClient") as mock_client:
            mock_client.return_value.search.return_value = FAKE_RESPONSE
            result = search("test query")
            assert result[0]["snippet"] == "Snippet 1"


def test_search_calls_tavily_with_query():
    with patch.dict(os.environ, {"TAVILY_API_KEY": "fake-key"}):
        with patch("tools.tavily.TavilyClient") as mock_client:
            mock_instance = mock_client.return_value
            mock_instance.search.return_value = FAKE_RESPONSE
            search("what is photosynthesis")
            mock_instance.search.assert_called_once_with(
                query="what is photosynthesis", search_depth="advanced", max_results=3
            )
