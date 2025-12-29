import asyncio
from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, IS_MEMBER
from aiogram import Router
from aiogram.types import ChatMemberUpdated

router = Router()

@router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def greet_new_member(event: ChatMemberUpdated):
    user_name = event.new_chat_member.user.first_name
    chat_name = event.chat.title
    
    await event.answer(
        f"Вітаємо, {user_name}, у чаті {chat_name}! 👋\n\n"
        f"Будь ласка, ознайомтеся з правилами. "
        f"Публікація оголошень дозволена лише після запрошення 3-х друзів."
    )