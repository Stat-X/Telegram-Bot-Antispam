from aiogram import Router, F
from aiogram.types import Message
from handlers.scaner_advertisement.model_setting import is_advertisment
from database.invite_posts_counts.right_to_post_smth import user_can_post 
from database import is_admin, plus_one_post


from database.invite_posts_counts.right_to_post_smth import check_and_plus_one_post

router = Router()

@router.message()
async def user_can_post_or_not(message: Message):
    await message.answer("Staring of ad-router")
    user = message.from_user
    
    # if await is_admin(user_id=user.id):
    #     return
    
    if await is_advertisment(message.text):
        
        await message.answer("This is Advertisment")
        
        
        if await check_and_plus_one_post(user.id):
            await message.answer(f"{message.from_user.first_name}, дякуємо за пост!")
        else:
            await message.answer(f"{message.from_user.first_name}, нажаль Ви не маєте права на пост.")
            
        # if await user_can_post(user_id=user.id):
        #     await message.answer(f'{message.from_user.first_name}, дякуємо за пост!')
        #     await plus_one_post(user_id=user.id)
        # else:
        #     await message.answer(f'{user.first_name}, нажаль Ви не маєте права на пост, бо не запросили достатньо людей.')
    
    else:
         await message.answer("This is not an  Advertisment")
       
   
