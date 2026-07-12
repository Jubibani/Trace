from dataclasses import dataclass
import os


def _env(name: str, default: str) -> str:
	value = os.getenv(name)
	return value if value else default


def _env_int(name: str, default: int) -> int:
	value = os.getenv(name)
	if not value:
		return default
	try:
		return int(value)
	except ValueError:
		return default


@dataclass(frozen=True)
class Settings:
	app_name: str = _env("APP_NAME", "Trace")
	app_version: str = _env("APP_VERSION", "0.1.0")
	app_env: str = _env("APP_ENV", "development")
	ollama_base_url: str = _env("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
	ollama_model: str = _env("OLLAMA_MODEL", "qwen2.5-coder:7b")
	ollama_timeout_seconds: int = _env_int("OLLAMA_TIMEOUT_SECONDS", 60)


settings = Settings()
