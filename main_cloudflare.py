#FastAPI
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import Request

#LLM endpoint
from llm.ollama_endpoint import call_ollama_chat,asyncio,parse_ollama_response
from llm.lm_studio_endpoint import call_lm_studio_chat,parse_lm_studio_response

#Schemas
#from schemas.ollama_scheme import ChatCompletionRequest, Response, ErrorResponse, get_available_models
from schemas.lm_studio_scheme import ChatCompletionRequest, Response, ErrorResponse, get_available_models


from config.config import PUBLIC_PORT

from pyngrok import ngrok
import uvicorn




app = FastAPI(title="FastAPI Wrapper for Ollama Chat")

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """处理请求验证错误"""
    error_msg = str(exc.errors()[0].get("msg")) if exc.errors() else "验证错误"
    return JSONResponse(
        status_code=400,
        content=ErrorResponse(
            detail=error_msg
        ).model_dump()
    )

@app.post("/chat", response_model=Response)
async def chat(request: ChatCompletionRequest):
    try:
        # 异步调用 Ollama API
        response = await call_lm_studio_chat(request.model, request.messages)
    except ValueError as e:
        return JSONResponse(
            status_code=400,
            content=ErrorResponse(
                detail=str(e),
                available_models=get_available_models()
            ).model_dump()
        )
    except asyncio.TimeoutError:
        raise HTTPException(status_code=504, detail="请求处理超时，请稍后再试")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ollama 调用失败: {e}")

    return Response(reply=await parse_lm_studio_response(response))

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PUBLIC_PORT)