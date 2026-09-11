from groq import APIError

from .client import client
from .config import (
    MODEL,
    REQUEST_TIMEOUT,
)
from .exceptions import LLMServiceUnavailableError
from .retry import retry_llm_request


def generate_response(prompt: str) -> str:
    if not prompt.strip():
        raise ValueError(
            "Prompt cannot be empty."
        )

    try:
        response = retry_llm_request(
            lambda: client.chat.completions.create(
                model=MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                timeout=REQUEST_TIMEOUT,
            )
        )

        return response.choices[0].message.content

    except APIError as error:
        raise LLMServiceUnavailableError(
            "The LLM service is currently unavailable."
        ) from error
