import os
import asyncio
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

API_KEY=os.getenv("API_OPEN_AI")

client = OpenAI(api_key=API_KEY)

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



