import aiosqlite

DB_PATH = 'database/users.db'

async def create_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY, 
                username TEXT,
                invitor_id INTEGER
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
        print('User Inserted')