import aiosqlite
from texts_to_use   import (
                            CREATE_DB_FOR_POSTS,
                            CREATE_DB_FOR_USERS, 
                            SQL_INSERT_USER_IN_DB_USERS,
                            SQL_INSERT_USER_IN_DB_POSTS
                          )

from env_collection import DB_PATH, DB_POST_PATH



async def create_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(CREATE_DB_FOR_USERS)
        await db.commit()


async def add_user(user_id, username):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(SQL_INSERT_USER_IN_DB_USERS,(user_id, username))
        await db.commit()

        
async def create_db_posts():
    async with aiosqlite.connect(DB_POST_PATH) as db:
        await db.execute(CREATE_DB_FOR_POSTS)
        await db.commit()


async def add_user_posts(user_id):
    async with aiosqlite.connect(DB_POST_PATH) as db:
        await db.execute(SQL_INSERT_USER_IN_DB_POSTS, (user_id,))
        await db.commit()
        