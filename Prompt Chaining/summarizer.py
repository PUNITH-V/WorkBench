from groq import Groq
from dotenv import load_dotenv
import os
import time


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Error: GROQ_API_KEY not found in environment variables.")

client = Groq(api_key=api_key)

def summarize_text(chunk_text:str) ->str:
    if not chunk_text.strip():
        return ""
    
    prompt = f"""
        Summarize ONLY the following text in a concise manner.

        Requirements:
        - Preserve names, facts, numbers, dates, and definitions.
        - Do not invent or infer information that is not present.
        - Keep the summary under 100 words.
        - If the text is already concise, return it as is.
        - Return ONLY the summary.
        - Do not add explanations or comments.

        Text:
        {chunk_text}
        """

    response = client.chat.completions.create(
        model ="openai/gpt-oss-20b",
        messages= [{
            "role": "user",
            "content": prompt
        }],
        temperature  = 0,
        reasoning_effort="low",
        max_completion_tokens=400
    )
    
    return response.choices[0].message.content


def summarize_chunks(chunks:list) -> list:
    result = []
    for chunk in chunks:
        summary = summarize_text(chunk['text'])
        result.append({
            "chunk_id": chunk['chunk_id'],
            "text": chunk['text'],
            "summary": summary,
            "source": chunk['source'],
            "page_number": chunk['page_number']
        })
        time.sleep(2)
    return result

def reduce_summaries(map_results:list)->str:
    labeled_summaries = []

    for result in map_results:
        labeled_summaries.append(
            f"Chunk{result['chunk_id']}, Page{result['page_number']}:\n"
            f"{result['summary']}"

        )
    combined_text = "\n\n".join(labeled_summaries)

    prompt = f"""
        Create one coherent final summary from the provided chunk summaries.

        Requirements:
        - Keep the final summary under 500 words.
        - Use ONLY facts present in the provided chunk summaries.
        - Do not invent or infer any information.
        - Organize the main ideas logically.
        - Cover every major topic represented by the chunk summaries.
        - Remove unnecessary repetition.
        - Return ONLY the final summary.
        - Do not mention the chunk numbers or the summarization process.

        Chunk summaries:
        {combined_text}
        """
    response = client.chat.completions.create(
        model = "openai/gpt-oss-20b",
        messages= [{
            "role": "user",
            "content": prompt
        }],
        temperature=0,
        reasoning_effort= "low",
        max_completion_tokens=800
    )
    return response.choices[0].message.content
