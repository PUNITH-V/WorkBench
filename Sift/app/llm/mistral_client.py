from mistralai.client import Mistral

from .client import LLMClient
from .retry import with_retry
from app.config.settings import settings


class MistralClient(LLMClient):

    @with_retry
    def generate(self, prompt: str) -> str:

        client = Mistral(
            api_key=settings.mistral_api_key
        )

        response = client.chat.complete(
            model=settings.mistral_model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content