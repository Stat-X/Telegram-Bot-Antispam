import os
import aiosqlite

from dotenv import load_dotenv
load_dotenv()

DB_PATH = os.getenv('DB_PATH')
DB_POST_INVITES_PATH = os.getenv('DB_POST_INVITES_PATH')

async def create_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY, 
                username TEXT,
                invitor_id INTEGER,
                invite_counts INTEGER DEFAULT 0,
                posts INTEGER DEFAULT 0,
                created_at TEXT DEFAULT (date('now'))  
            ) 
            """
        )
        await db.commit()


async def add_user(user_id, username):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)",
            (user_id, username) 
        )
        await db.commit()
        print('User Inserted into USERS')
        








async def create_db_of_invites_and_posts():
    async with aiosqlite.connect(DB_POST_INVITES_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS post_invites (
                user_id INTEGER PRIMARY KEY, 
                posts INTEGER DEFAULT 0
            ) 
            """
        )
        await db.commit()



async def add_user_posts_invites(user_id):
    async with aiosqlite.connect(DB_POST_INVITES_PATH) as db:
        await db.execute(
            "INSERT OR IGNORE INTO post_invites (user_id) VALUES (?)",
            (user_id,) 
        )
        await db.commit()
        print('User Inserted into INVITED POSTS')