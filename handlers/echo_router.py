import asyncio
from aiogram import Router, types

router = Router()

@router.message()
async def echo(msg: types.Message):
    await msg.answer(msg.text) 
        