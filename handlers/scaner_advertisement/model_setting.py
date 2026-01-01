import os
import asyncio
from openai import OpenAI
from env_collection import API_OPEN_AI



client = OpenAI(api_key=API_OPEN_AI)

async def is_advertisement(text: str, prompt: str) -> bool:
    
    ready_prompt = prompt + text 
    
    
    loop = asyncio.get_running_loop()
    response = await loop.run_in_executor(
        None,
        lambda: client.responses.create(
            model="gpt-5-nano",
            input=ready_prompt
        )
    )
    return bool(int(response.output_text.strip()))



