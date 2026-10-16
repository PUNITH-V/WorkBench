import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "openrouter/free"
BASE_URL = "https://openrouter.ai/api/v1"

if not API_KEY:
    raise ValueError(
        "OPENROUTER_API_KEY is missing."
        "Add it to your .env file"
    )
