import os
from dotenv import load_dotenv
from aiogram import F, Router, types
from handlers.antilink_regex import LINK_REGEX, LOCALHOST_REGEX

load_dotenv()

ADMIN=os.getenv('ADMIN')

router = Router()

@router.message(F.text)
async def handle_links(message: types.Message):
    
    has_embedded_link = any(e.type == "text_link" for e in message.entities or [])
    has_url_entity = any(e.type == "url" for e in message.entities or [])
    
    if (
        LINK_REGEX.search(message.text) 
        or LOCALHOST_REGEX.search(message.text)
        or has_embedded_link
        or has_url_entity  
    ):
        await message.delete()
        await message.answer(f"{message.from_user.first_name}, скидати посилання в чат заборонено")
    
