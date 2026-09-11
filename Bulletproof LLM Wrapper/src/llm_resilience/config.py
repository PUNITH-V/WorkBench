import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError(
        "API KEY is not set yet"
        "Once check .env File"
    )

MODEL = "openai/gpt-oss-20b"

REQUEST_TIMEOUT = 5.0
MAX_RETRIES = 3

BACKOFF_MULTIPLIER = 1
MIN_BACKOFF = 2
MAX_BACKOFF = 10
