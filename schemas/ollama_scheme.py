from pydantic import BaseModel, ValidationError, field_validator
import ollama
from functools import lru_cache
from typing import List, Optional

allowed_roles = ["user", "assistant","system"]

#add some refresh scheme maybe?
@lru_cache(maxsize=1)
def get_available_models() -> List[str]:
        return [model.model for model in ollama.list().models]


class ChatMessage(BaseModel):
    role: str
    content: str

    @field_validator("role")
    @classmethod
    def validate_role(cls, v):
        if v not in allowed_roles:
            raise ValueError(f"Invalid role: {v}. Must be one of {allowed_roles}.")
        return v
    
class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    temperature: Optional[float] = None

    @field_validator('model')
    @classmethod
    def validate_model(cls, v):
        try:
            allowed_models = get_available_models()
        except ConnectionError as e:
            raise ValueError("ollama server is not running")
        
        if not allowed_models:
            raise ValueError("no model is downloaded in the server")
        if v not in allowed_models:
            raise ValueError(
                f"unavailable model: {v}\n"
            )
        return v

class Response(BaseModel):
    reply: str
    
class ErrorResponse(BaseModel):
    """错误响应模型"""
    detail: str
    available_models: List[str] = []