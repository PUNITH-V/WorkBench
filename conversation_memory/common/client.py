from typing import List, Dict

from groq import Groq


Message = Dict[str, str]


class GroqClient:
    """
    Wrapper around the Groq chat completion API.
    """

    def __init__(self, api_key: str, model: str):
        if not api_key:
            raise ValueError("API key cannot be empty.")

        if not model:
            raise ValueError("Model cannot be empty.")

        self.model = model

        try:
            self.client = Groq(api_key=api_key)
        except Exception as exc:
            raise RuntimeError(
                f"Failed to initialize Groq client: {exc}"
            ) from exc

    def get_response(self, messages: List[Message]) -> str:
        """
        Send messages to Groq and return the assistant response.
        """

        if not messages:
            raise ValueError(
                "Messages cannot be empty."
            )

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )

        except Exception as exc:
            raise RuntimeError(
                f"Groq API request failed: {exc}"
            ) from exc

        if not response:
            raise RuntimeError(
                "Groq returned an empty response."
            )

        if not response.choices:
            raise RuntimeError(
                "Groq response contains no choices."
            )

        message = response.choices[0].message

        if not message:
            raise RuntimeError(
                "Groq response contains no message."
            )

        content = message.content

        if not content:
            raise RuntimeError(
                "Groq returned an empty assistant response."
            )

        return content.strip()
    