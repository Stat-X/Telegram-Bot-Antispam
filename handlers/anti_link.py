import os
from dotenv import load_dotenv
from aiogram import F, Router, types

load_dotenv()

ADMIN=os.getenv('ADMIN')

router = Router()


# @router.message(F.entities.any(F.type.in_({'url', 'text_link'})))
# async def handle_links(message: types.Message):
#     print('I saw a link')
#     await message.answer('This is a link')
    
    
@router.message(
    (F.entities.any(F.type.in_({'url', 'text_link'}))) | 
    (F.text.contains("http://")) | 
    (F.text.contains("https://")) |
    (F.text.contains("t.me/"))
)
async def handle_links(message: types.Message):
    
    if message.from_user.username == ADMIN:
        return
    
    print('Я побачив посилання!')
    await message.delete()
    await message.answer(f"@{message.from_user.username}, посилання заборонені!")


