import aiosqlite
from database     import DB_PATH
from texts_to_use import SQL_IS_IN_DB_CHECK


async def is_in_db(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(SQL_IS_IN_DB_CHECK, (user_id,)) as cursor:
            result = await cursor.fetchone()
            return result is not None
            
