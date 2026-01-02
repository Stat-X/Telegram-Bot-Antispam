import asyncio
from aiogram  import Bot, Dispatcher
from handlers import welcome_router, antispam_router, farewell_router, del_tg_msg_router
from database import create_db, create_db_posts
from env_collection import TOKEN          


bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    await create_db()
    await create_db_posts()
    dp.include_router(del_tg_msg_router)
    dp.include_router(welcome_router)
    dp.include_router(farewell_router)
    dp.include_router(antispam_router)
    await dp.start_polling(bot)

    
if __name__ == "__main__":
    print("The bot began working")
    asyncio.run(main())
    
