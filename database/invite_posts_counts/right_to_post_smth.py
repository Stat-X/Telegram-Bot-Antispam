import aiosqlite
from database import DB_PATH, INVITES_TO_POST


async def user_can_post(user_id):
    invited, posts = await invited_and_posts(userd_id=user_id)
    post_may_do = invited//INVITES_TO_POST  
    return post_may_do > posts


async def invited_and_posts(userd_id):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("""
                              SELECT
                                invite_counts,
                                posts 
                              FROM 
                                users 
                              WHERE 
                                user_id = ?;""", (userd_id,)
                            ) as cursor:
            
            result = await cursor.fetchone()
            
            if result:
                invited, posts = result  
                return invited, posts
            return 0, 0  







from filelock import FileLock
import aiosqlite

DB_PATH = DB_PATH
INVITES_TO_POST = 3  # твоя константа
file_lock = FileLock("db.sqlite.lock")

async def check_and_plus_one_post(user_id: int) -> bool:
    """
    Перевіряє, чи користувач може зробити пост,
    і одразу збільшує лічильник постів, якщо можна.
    Повертає True, якщо пост дозволено, False — якщо ні.
    """
    with file_lock:  # блокування для всіх процесів
        async with aiosqlite.connect(DB_PATH) as db:
            # 1️⃣ SELECT
            async with db.execute(
                "SELECT invite_counts, posts FROM users WHERE user_id = ?",
                (user_id,)
            ) as cursor:
                result = await cursor.fetchone()
                invited, posts = result if result else (0, 0)

            # 2️⃣ Перевірка права
            post_may_do = invited // INVITES_TO_POST
            if post_may_do > posts:
                # 3️⃣ UPDATE
                await db.execute(
                    "UPDATE users SET posts = posts + 1 WHERE user_id = ?",
                    (user_id,)
                )
                await db.commit()
                return True

            return False