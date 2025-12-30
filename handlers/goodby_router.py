from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, IS_MEMBER
from aiogram import Router
from aiogram.types import ChatMemberUpdated
from database import add_user
from database import is_in_db

router = Router()

@router.chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
async def goodby_user(event: ChatMemberUpdated):
    
    user = event.old_chat_member.user
    user_id = user.id
    username = user.username
    chat_name = event.chat.title
    
    await event.answer(
        f"""{user.first_name} покинув чат :( \nСподіваємось на Ваше повернення"""
    )
    
    if not await is_in_db(user_id):
        await add_user(user_id=user_id, username=username)
    