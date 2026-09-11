from unittest.mock import Mock

from groq import APITimeoutError

from llm_resilience.retry import retry_llm_request


def test_timeout_is_retried():

    mock_api = Mock(
        side_effect=[
            APITimeoutError(
                "Request timed out"
            ),
            APITimeoutError(
                "Request timed out"
            ),
            "Success",
        ]
    )

    result = retry_llm_request(mock_api)

    assert result == "Success"

    assert mock_api.call_count == 3
