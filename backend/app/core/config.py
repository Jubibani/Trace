from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("LCIA_APP_NAME", "Local Code Intelligence Assistant")
    app_env: str = os.getenv("LCIA_ENV", "development")
    app_version: str = os.getenv("LCIA_VERSION", "0.1.0")
    ollama_base_url: str = os.getenv("OLLAMA_HOST", os.getenv("LCIA_OLLAMA_BASE_URL", "http://localhost:11434"))
    ollama_model: str = os.getenv("LCIA_OLLAMA_MODEL", "qwen2.5-coder:7b")
    ollama_timeout_seconds: float = float(os.getenv("LCIA_OLLAMA_TIMEOUT_SECONDS", "60"))


settings = Settings()
