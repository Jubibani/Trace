from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.llm_service import LLMServiceError, llm_service


class ChatRequest(BaseModel):
	message: str = Field(min_length=1)
	model: str | None = None


class ChatResponse(BaseModel):
	model: str
	response: str


router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
	try:
		result = await llm_service.chat(
			messages=[{"role": "user", "content": request.message}],
			model=request.model,
		)
	except LLMServiceError as exc:
		raise HTTPException(status_code=502, detail=str(exc)) from exc

	return ChatResponse(model=result.model, response=result.content)
