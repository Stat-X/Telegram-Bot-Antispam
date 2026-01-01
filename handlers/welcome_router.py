from aiogram         import Router
from aiogram.types   import ChatMemberUpdated
from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, IS_MEMBER

from database import (
                      add_user, 
                      is_in_db, 
                      invite_is_valid_to_count, 
                      plus_one_to_ivites_of_inviter, 
                      add_user_posts
                    )

from texts_to_use import WELCOME_MESSAGE_FOR_OLD, WELCOME_MESSAGE_FOR_NEW

router = Router()

@router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def greet_new_member(event: ChatMemberUpdated):
    user = event.new_chat_member.user
    chat_name = event.chat.title
    
    if await invite_is_valid_to_count(event=event):
        await plus_one_to_ivites_of_inviter(event=event)
         
    if not await is_in_db(user_id=user.id):
        await event.answer(
            WELCOME_MESSAGE_FOR_NEW.format(
                first_name=user.first_name, chat_name=chat_name
                )
            )
        
        await add_user(user_id=user.id, username=user.username)
        await add_user_posts(user_id=user.id)
        
    else:
        await event.answer(
            WELCOME_MESSAGE_FOR_OLD.format(
                first_name=user.first_name, chat_name=chat_name
                )
            )
        
        
        