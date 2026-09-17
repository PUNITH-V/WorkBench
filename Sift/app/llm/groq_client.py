from groq import Groq
from .client import LLMClient
from app.config.settings import settings
from .retry import with_retry


class GroqClient(LLMClient):
    @with_retry
    def generate(self,prompt:str) ->str:
        client = Groq(api_key = settings.groq_api_key)

        response = client.chat.completions.create(
            model = settings.groq_model,
            messages = [{"role":"user","content":prompt}]
        )
        return response.choices[0].message.content
    