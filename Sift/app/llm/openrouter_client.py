from openai import OpenAI

from .client import LLMClient
from .retry import with_retry
from app.config.settings import settings


class OpenRouterClient(LLMClient):

    @with_retry
    def generate(self, prompt: str) -> str:

        client = OpenAI(
            api_key=settings.openrouter_api_key,
            base_url="https://openrouter.ai/api/v1",
        )

        response = client.chat.completions.create(
            model=settings.openrouter_model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content