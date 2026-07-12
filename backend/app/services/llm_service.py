from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import httpx

from app.core.config import settings


@dataclass(frozen=True)
class ChatResult:
	model: str
	content: str
	raw: dict[str, Any]


class LLMServiceError(RuntimeError):
	pass


class LLMService:
	def __init__(self, base_url: str | None = None, timeout_seconds: float | None = None) -> None:
		self.base_url = base_url or settings.ollama_base_url
		self.timeout_seconds = timeout_seconds or settings.ollama_timeout_seconds

	async def chat(
		self,
		messages: list[dict[str, str]],
		model: str | None = None,
	) -> ChatResult:
		payload = {
			"model": model or settings.ollama_model,
			"messages": messages,
			"stream": False,
		}

		try:
			async with httpx.AsyncClient(base_url=self.base_url, timeout=self.timeout_seconds) as client:
				response = await client.post("/api/chat", json=payload)
				response.raise_for_status()
		except httpx.HTTPError as exc:
			raise LLMServiceError(f"Failed to call Ollama at {self.base_url}: {exc}") from exc

		data = response.json()
		message = data.get("message") or {}

		return ChatResult(
			model=data.get("model", payload["model"]),
			content=message.get("content", ""),
			raw=data,
		)


llm_service = LLMService()
