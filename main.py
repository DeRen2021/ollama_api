from fastapi import FastAPI, HTTPException
from fastapi.concurrency import run_in_threadpool
from contextlib import asynccontextmanager

from schemas.ollama_scheme import Message, Response, ErrorResponse, get_available_models
import ollama
import asyncio

from config.config import NGROK_DOMAIN, NGROK_AUTHTOKEN

from pyngrok import ngrok
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import Request

@asynccontextmanager
async def lifespan(app: FastAPI):
    tunnels = ngrok.connect(8000, domain=NGROK_DOMAIN, bind_tls=True)
    print(f"ngrok tunnel established at https://{NGROK_DOMAIN}")
    yield
    ngrok.kill()

app = FastAPI(title="FastAPI Wrapper for Ollama Chat",lifespan=lifespan)

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
async def chat(request: Message):
    try:
        response = await asyncio.wait_for(
            run_in_threadpool(
                ollama.chat,
                request.model,
                messages=[{'role': 'user', 'content': request.message}]
            ),
            timeout= 90
        )
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
    return Response(reply=response.message.content)

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)