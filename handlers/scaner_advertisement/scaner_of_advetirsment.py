from aiogram.types import Message
from handlers.scaner_advertisement.model_setting import is_advertisement
from database.invite_posts_counts.right_to_post_smth import user_can_post 
from database import is_admin, plus_one_post



async def user_can_post_or_not(message: Message):
    # await message.answer("Staring of ad-router")
    user = message.from_user
    
    # if await is_admin(user_id=user.id):
    #     return
    
    if await is_advertisement(message.text):
        
        # await message.answer("This is Advertisment")
          
        if await user_can_post(user_id=user.id):
            await message.answer(f'{message.from_user.first_name}, дякуємо за пост😃\n Щоб зробити настпуний - запросіть ще 3х людей в чат😎')
            await plus_one_post(user_id=user.id)
        else:
            await message.delete()
            await message.answer(f"""
{user.first_name}, нажаль Ви не маєте права на пост, бо не запросили достатньо людей☹ \n\n Пам'ятайте - кожен пост коштує 3 запрошення😁""")
    
    else:
        #  await message.answer("This is not an  Advertisment")
        pass
       
   
