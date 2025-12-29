import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router, types


load_dotenv()


bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(message.text)
    
router = Router()

@router.message("HI")
async def echo_handler(message: types.Message):
    await message.answer("Hello!")

async def main():
    # dp.include_router(router)
    await router.start_polling(bot)
    
    
if __name__ == "__main__":
    asyncio.run(main())
