from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    groq_api_key: str
    groq_model: str = "groq/compound"

    mistral_api_key: str
    mistral_model: str = "mistral-small-2603"

    openrouter_api_key : str
    openrouter_model : str = "openrouter/free"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()