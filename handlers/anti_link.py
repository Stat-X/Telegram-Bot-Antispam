import os
from dotenv import load_dotenv
from aiogram import F, Router, types
from handlers.antilink_regex import LINK_REGEX, LOCALHOST_REGEX

load_dotenv()

ADMIN=os.getenv('ADMIN')

router = Router()

@router.message(F.text)
async def handle_links(message: types.Message):
    if LINK_REGEX.search(message.text):
        await message.delete()
        await message.answer(f"{message.from_user.first_name}, скидати посилання в чат заборонено")
    elif LOCALHOST_REGEX.search(message.text):
        await message.delete()
        await message.answer(f"{message.from_user.first_name}, скидати посилання в чат заборонено")
