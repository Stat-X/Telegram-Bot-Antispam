# import asyncio
from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, IS_MEMBER
from aiogram import Router
from aiogram.types import ChatMemberUpdated
from database import add_user, is_in_db, invite_is_valid_to_count, plus_one_to_ivites_of_inviter


router = Router()


@router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def greet_new_member(event: ChatMemberUpdated):
    user = event.new_chat_member.user
    chat_name = event.chat.title
    
    if await invite_is_valid_to_count(event=event):
        await plus_one_to_ivites_of_inviter(event=event)
        await event.answer('This invite was valid')
        
    else:
        await event.answer("This invite is not valid")
        pass
    
    if not await is_in_db(user_id=user.id):
        await event.answer(
            f"Вітаємо, {user.first_name}, у чаті {chat_name}! 👋\n\n"
            f"Будь ласка, ознайомтеся з правилами. "
            f"Публікація оголошень дозволена лише після запрошення 3-х друзів."
        )
        
        await add_user(user_id=user.id, username=user.username)
        
    else:
        await event.answer(
            f"З поверненням, {user.first_name}. Раді Вас знову бачити у чаті {chat_name}! 👋\n\n" 
        )
        
        
        