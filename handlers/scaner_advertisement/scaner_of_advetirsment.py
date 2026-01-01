from aiogram  import types
from database import is_admin, plus_one_post
from handlers.scaner_advertisement.model_setting     import is_advertisement
from database.invite_posts_counts.right_to_post_smth import user_can_post 

from texts_to_use import (
                          PROMPT_TEMPLATE, 
                          THANKS_FOR_POST, 
                          SORRY_YOU_CANT_POST
                         )


async def user_can_post_or_not(message: types.Message):
    user = message.from_user
    
    text = message.text or message.caption
    
    if await is_advertisement(text, prompt=PROMPT_TEMPLATE):
              
        if await user_can_post(user_id=user.id):
            
            await message.answer(
                THANKS_FOR_POST.format(
                    first_name=user.first_name
                    )
                )
            
            await plus_one_post(user_id=user.id)
            
        else:
            await message.delete()
            
            await message.answer(
                SORRY_YOU_CANT_POST.format(
                    first_name=user.first_name
                    )
                )

    
    
       
   
