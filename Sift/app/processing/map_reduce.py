from app.llm.client import LLMClient
from app.processing.chunker import chunk_text
from app.processing.summarizer import summarize_chunk


def map_reduce(
    llm: LLMClient,
    text: str,
) -> str:

    chunks = chunk_text(text)

    summaries = []

    for i, chunk in enumerate(chunks, 1):
        print(f"  Summarizing chunk {i}/{len(chunks)}...")
        summary = summarize_chunk(llm, chunk)
        summaries.append(summary)

    combined_summaries = "\n\n".join(summaries)

    reduce_prompt = f"""
Write a concise factual summary of the article using the section
summaries below.

Rules:
- Return ONLY the summary itself.
- Do not mention the section summaries.
- Do not mention the instructions or the task.
- Do not describe your reasoning or process.
- Do not use phrases like "Based on the provided summaries",
  "Here is a summary", "I will", "I need to", or "Let me".
- Do not add information that is not present in the section summaries.
- Combine repeated information.
- Preserve important facts, claims, and details.
- Write in clear paragraphs.
- Do not use headings such as "Main Idea", "Key Claims", or
  "Important Details".

Section summaries:

{combined_summaries}
"""

    summary = llm.generate(reduce_prompt)

    if not summary.strip():
        raise ValueError("LLM returned an empty final summary")
    return summary.strip()