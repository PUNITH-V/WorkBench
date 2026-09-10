from ollama import chat
from prompt_template import extraction_prompt
from schemas import SupportTicket


def extract_support_ticket(transcript: str) -> SupportTicket:
    prompt = extraction_prompt(transcript)
    response = chat(
               model = "qwen2.5:3b-instruct",
               messages= [{"role": "user", "content": prompt}],
               format = SupportTicket.model_json_schema(),
               options = {"temperature": 0.0}

    )
    ticket = SupportTicket.model_validate_json(response.message.content)
    return ticket
