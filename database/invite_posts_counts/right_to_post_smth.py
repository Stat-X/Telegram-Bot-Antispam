import aiosqlite
from database     import DB_PATH, DB_POST_PATH, INVITES_TO_POST
from texts_to_use import SQL_INVITES_COUNT, SQL_POST_COUNT


async def user_can_post(user_id):
    invited = await invited_by_user(user_id=user_id)
    posts = await posts_of_user(user_id=user_id)
    post_may_do = invited//INVITES_TO_POST  
    return post_may_do > posts


async def invited_by_user(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(SQL_INVITES_COUNT, (user_id,)) as cursor:
            result = await cursor.fetchone()
            if result:
                invited = result[0] 
                return invited
            return 0


async def posts_of_user(user_id):
    async with aiosqlite.connect(DB_POST_PATH) as db:
        async with db.execute(SQL_POST_COUNT, (user_id,)) as cursor:
            result = await cursor.fetchone()
            if result:
                posts = result[0] 
                return posts
            return 0




