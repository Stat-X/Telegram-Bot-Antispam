import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import welcome_router, link_router, farewell_router
from database import create_db, create_db_of_invites_and_posts


load_dotenv()


bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

    

async def main():
    await create_db()
    await create_db_of_invites_and_posts()
    dp.include_router(link_router)
    dp.include_router(farewell_router)
    dp.include_router(welcome_router)
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    asyncio.run(main())
