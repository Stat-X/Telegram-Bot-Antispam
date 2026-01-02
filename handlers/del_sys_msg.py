from aiogram import F, Router
from aiogram.types import Message

router = Router()

@router.message(F.new_chat_members | F.left_chat_member)
async def delete_system_join(message: Message):
    try:
        await message.delete()
    except Exception:
        pass
    
router_ = Router()

@router.message(F.chat.type == "private")
async def block_private_messages(message: Message):
    try:
        await message.delete()
    except Exception:
        pass