from app.llm.client import LLMClient


def summarize_research(
    llm: LLMClient,
    article_summaries: list[str],
) -> str:

    combined = "\n\n".join(article_summaries)

    prompt = f"""
Create one concise overall research summary from the
following article summaries.

Identify:
- The main theme
- The most important findings
- Important differences or common points

Rules:
- Return only the final summary.
- Do not explain your reasoning.
- Do not describe the task or these instructions.
- Do not say "I need to", "Let me", or similar phrases.
- Do not add information that is not present in the summaries.
- Do not include analysis of how you created the summary.

Article summaries:

{combined}
"""
    
    return llm.generate(prompt)