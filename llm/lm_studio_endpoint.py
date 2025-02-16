from openai import OpenAI
from config.config import BASE_URL, LM_STUDIO_PORT

async def call_lm_studio_chat(model, messages):
    client = OpenAI(base_url=f"http://localhost:1234/v1",api_key="not_needed")
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response


async def parse_lm_studio_response(response):
    return response.choices[0].message.content