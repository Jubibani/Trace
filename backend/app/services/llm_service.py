from __future__ import annotations

from dataclasses import dataclass
import httpx

from ..core.config import settings


@dataclass(frozen=True)
class ChatResult:
	message: str
	model: str
	source: str


class LLMService:
	def __init__(
		self,
		base_url: str | None = None,
		model: str | None = None,
		timeout_seconds: int | None = None,
	) -> None:
		self.base_url = base_url or settings.ollama_base_url
		self.model = model or settings.ollama_model
		self.timeout_seconds = timeout_seconds or settings.ollama_timeout_seconds

	async def generate(self, prompt: str) -> ChatResult:
		prompt = prompt.strip()
		if not prompt:
			return ChatResult(
				message="Please provide a prompt to trace.",
				model=self.model,
				source="fallback",
			)

		payload = {
			"model": self.model,
			"prompt": prompt,
			"stream": False,
		}

		try:
			async with httpx.AsyncClient(timeout=self.timeout_seconds) as client:
				response = await client.post(f"{self.base_url}/api/generate", json=payload)
				response.raise_for_status()
		except httpx.HTTPError as error:
			return ChatResult(
				message=(
					"Could not reach local Ollama runtime. "
					"Ensure Ollama is running and the model is pulled. "
					f"Details: {error}"
				),
				model=self.model,
				source="fallback",
			)

		data = response.json()
		message = data.get("response", "").strip()
		if not message:
			return ChatResult(
				message="Ollama returned an empty response.",
				model=self.model,
				source="fallback",
			)

		return ChatResult(message=message, model=self.model, source="ollama")
