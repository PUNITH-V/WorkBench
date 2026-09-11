from unittest.mock import MagicMock, patch

from llm_resilience.llm import generate_response


@patch("llm_resilience.llm.client")
def test_generate_response(mock_client):

    mock_response = MagicMock()

    mock_response.choices[0].message.content = (
        "Hello from the AI!"
    )

    mock_client.chat.completions.create.return_value = (
        mock_response
    )

    result = generate_response(
        "Say hello"
    )

    assert result == "Hello from the AI!"
