import os 


class ConfigError(Exception):
    pass

def get_api_key() -> str:
    api_key =os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ConfigError(
            "GROQ_API_KEY environment variable is not set."
        )

    api_key = api_key.strip()

    if not api_key:
        raise ConfigError(
            "GROQ_API_KEY cannot be empty."
        )
    return api_key

def get_model() -> str:

    model = os.getenv(
        "GROQ_MODEL",
        "llama-3.3-70b-versatile"
    )

    if not model.strip():
        raise ConfigError(
            "GROQ_MODEL cannot be empty"
        )
    return model.strip()

def get_system_prompt() -> str:

    return os.getenv(
        "SYSTEM_PROMPT",
        "You are a helpful assistant."
    )

def get_memory_limit() -> int:

    value = os.getenv("MEMORY_LIMIT", "10")

    try:
        limit = int(value)
        
    except ValueError as exc:
        raise ConfigError(
            "MEMORY_LIMIT must be an integer."
        ) from exc

    if limit < 5:
        raise ConfigError(
            "MEMORY_LIMIT must be at least 5."
        )

    return limit

