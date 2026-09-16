from app.llm.openrouter_client import OpenRouterClient

llm = OpenRouterClient()

print(llm.generate("Say hello in one sentence."))