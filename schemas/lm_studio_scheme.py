from pydantic import BaseModel, ValidationError, field_validator
import ollama
from typing import List, Optional
from functools import lru_cache
import requests
allowed_roles = ["user", "assistant","system"]


@lru_cache(maxsize=1)
def get_available_models() -> List[str]:

    url = "http://localhost:1234/v1/models"
    response = requests.get(url)
    if response.ok:
        return [i['id'] for i in response.json()['data']]
    else:
        return []


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
            raise ValueError("lm_studio server is not running")
        
        if not allowed_models:
            raise ValueError("no model is downloaded in the server")
        if v not in allowed_models:
            raise ValueError(
                f"unavailable model: {v}\n available models: {allowed_models}"
            )
        return v

class Response(BaseModel):
    reply: str
    
class ErrorResponse(BaseModel):
    """错误响应模型"""
    detail: str
    available_models: List[str] = []