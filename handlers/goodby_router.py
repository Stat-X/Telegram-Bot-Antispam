import asyncio
from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, IS_MEMBER
from aiogram         import Router
from aiogram.types   import ChatMemberUpdated
from database        import add_user, add_user_posts
from database        import is_in_db
from texts_to_use    import GOODBY_MESSAGE
from env_collection  import TIME_BEFORE_DELETING_FAREWELL_MSG

from handlers.msg_deleter import delete_after

router = Router()

@router.chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
async def goodby_user(event: ChatMemberUpdated):
    
    user = event.old_chat_member.user
    user_id = user.id
    username = user.username
    
    msg = await event.answer(GOODBY_MESSAGE.format(first_name=user.first_name))
    
    asyncio.create_task(delete_after(msg=msg, delay=TIME_BEFORE_DELETING_FAREWELL_MSG))
    
    if not await is_in_db(user_id):
        await add_user(user_id=user_id, username=username)
        await add_user_posts(user_id=user_id)
    