from fastapi import APIRouter
from pydantic import BaseModel, Field

from ..services.llm_service import LLMService

router = APIRouter(tags=["chat"])


class ChatRequest(BaseModel):
	message: str = Field(min_length=1, description="User prompt for the assistant")


class ChatResponse(BaseModel):
	message: str
	model: str
	source: str


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
	service = LLMService()
	result = await service.generate(request.message)
	return ChatResponse(message=result.message, model=result.model, source=result.source)
