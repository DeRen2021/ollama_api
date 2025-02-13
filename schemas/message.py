from pydantic import BaseModel, ValidationError, field_validator
import ollama
from functools import lru_cache
from typing import List

#add some refresh scheme maybe?
@lru_cache(maxsize=1)
def get_available_models() -> List[str]:
        return [model.model for model in ollama.list().models]


class Message(BaseModel):
    model: str
    message: str

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