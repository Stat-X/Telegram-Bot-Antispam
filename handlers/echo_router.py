import asyncio
from aiogram import Router, types, F

router = Router()

@router.message()
async def echo(msg: types.Message):
    if msg.text is None:
        return 
        
    await msg.answer(msg.text)

        