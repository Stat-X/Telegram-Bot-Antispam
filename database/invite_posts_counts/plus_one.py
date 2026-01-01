import aiosqlite
from database       import  (
                            is_in_db, 
                            add_user, 
                            add_user_posts
                           )

from env_collection import DB_PATH, DB_POST_PATH

from texts_to_use   import (
                            SQL_UPDATE_PLUS_ONE_POST, 
                            SQL_UPDATE_PLUS_ONE_INVITE
                           )

from aiogram.types  import ChatMemberUpdated



async def plus_one_to_ivites_of_inviter(event: ChatMemberUpdated):
    inviter = event.from_user
    
    if not await is_in_db(inviter.id):
        await add_user(user_id=inviter.id, username=inviter.username)
        await add_user_posts(user_id=inviter.id)
    
    await plus_one_invite(inviter_id=inviter.id)
    
    
async def plus_one_invite(inviter_id):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(SQL_UPDATE_PLUS_ONE_INVITE, (inviter_id,))
        await db.commit()


async def plus_one_post(user_id):
    async with aiosqlite.connect(DB_POST_PATH) as db:
        await db.execute(SQL_UPDATE_PLUS_ONE_POST,(user_id,))
        await db.commit()
