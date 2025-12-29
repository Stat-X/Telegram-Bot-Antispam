import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router, types
from handlers import welcome_router, echo_router


load_dotenv()


bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

    

async def main():
    dp.include_router(welcome_router)
    dp.include_router(echo_router)
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    asyncio.run(main())
