from aiogram import F, Router
from aiogram.types import Message

router = Router()

@router.message(F.new_chat_members | F.left_chat_member)
async def delete_system_join(message: Message):
    try:
        await message.delete()
    except Exception:
        pass