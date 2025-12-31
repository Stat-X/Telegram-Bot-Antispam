import aiosqlite
from database import is_in_db, add_user, DB_PATH
from aiogram.types import ChatMemberUpdated


async def plus_one_to_ivites_of_inviter(event: ChatMemberUpdated):
    inviter = event.from_user
    
    if not await is_in_db(inviter.id):
        await add_user(user_id=inviter.id, username=inviter.username)
    
    await plus_one_invite(inviter_id=inviter.id)


async def plus_one_invite(inviter_id):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
                            UPDATE 
                                users 
                            SET 
                                invite_counts = invite_counts + 1 
                            WHERE user_id = ?
                        """,        
                        (inviter_id,)            
                        )
        await db.commit()
        print(str(inviter_id) + " Inviter got 1")

