from aiogram.filters import ChatMemberUpdatedFilter
from aiogram.types import ChatMemberUpdated
from aiogram.enums import ChatMemberStatus
from database.is_already_in_db_check import is_in_db


not_count_invite_from = {ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR}


async def invite_is_valid_to_count(event: ChatMemberUpdated):
    
    #if no inviter - automatically invalid to count this as an invite
    inviter = event.from_user
    
    if not inviter:
        await event.answer('No inviter')
        return False
    
    inviter_id = inviter.id
    joined_user = event.new_chat_member.user
    
    #1 invite is valid if user did not come himself 
    if inviter_id == joined_user.id:
        await event.answer('Inviter == Joined')
        return False 
    
    # 2  invite is valid if the user was not in db before the invite
    # if await is_in_db(joined_user.id):
    #     await event.answer('Already in DB')
    #     return False
    
    # 3 invite is valid if it was not an invite from an admin
    # if await is_admin(event, inviter_id):
    #     await event.answer('Admin added')
    #     return False
    
    await event.answer(f"Inviter {event.from_user.username}")
    return True
    
   
async def is_admin(event, user_id):
    member = await event.bot.get_chat_member(event.chat.id, user_id)
    if member.status in not_count_invite_from:
        return True
    
 
    
    
   
    



   
    