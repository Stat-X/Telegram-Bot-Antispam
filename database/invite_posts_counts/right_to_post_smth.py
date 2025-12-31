import aiosqlite
from database import DB_PATH, DB_POST_INVITES_PATH, INVITES_TO_POST


async def user_can_post(user_id):
    invited = await invited_by_user(user_id=user_id)
    posts = await posts_of_user(user_id=user_id)
    post_may_do = invited//INVITES_TO_POST  
    return post_may_do > posts


async def invited_by_user(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("""
                              SELECT
                                invite_counts 
                              FROM 
                                users 
                              WHERE 
                                user_id = ?;""", (user_id,)
                            ) as cursor:
            
            result = await cursor.fetchone()
            
            if result:
                invited = result[0] 
                return invited
            return 0


async def posts_of_user(user_id):
    async with aiosqlite.connect(DB_POST_INVITES_PATH) as db:
        async with db.execute("""
                              SELECT
                                posts 
                              FROM 
                                post_invites 
                              WHERE 
                                user_id = ?;""", (user_id,)
                            ) as cursor:
            
            result = await cursor.fetchone()
            
            if result:
                posts = result[0] 
                return posts
            return 0




