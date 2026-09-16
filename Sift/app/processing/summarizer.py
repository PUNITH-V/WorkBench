from app.llm.client import LLMClient


def summarize_chunk(
    llm: LLMClient,
    text: str,
) -> str:

    prompt = f"""
Summarize the following section of an article.

Rules:
- Return ONLY factual content from the section.
- Do not talk about the task or the instructions.
- Do not describe your reasoning or process.
- Do not say "Here is a summary", "Based on", "I will", "I need to",
  "Let me", or similar meta-commentary.
- Do not add information that is not present in the section.
- Preserve important facts, claims, names, numbers, and details.
- Focus on the main ideas and information that would be useful
  when reconstructing the complete article.

Article section:

{text}
"""

    return llm.generate(prompt)