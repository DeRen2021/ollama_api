import ollama
from ollama import AsyncClient
import asyncio

async def call_ollama_chat(model, messages):
    client = AsyncClient()
    response = await asyncio.wait_for(
        client.chat(model=model, messages=messages),
        timeout=90
    )
    return response


async def parse_ollama_response(response):
    return response.message.content