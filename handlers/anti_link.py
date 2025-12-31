from aiogram import F, Router, types
from handlers.antilink_regex import LINK_REGEX, LOCALHOST_REGEX
from database import is_admin
from handlers.scaner_advertisement.scaner_of_advetirsment import user_can_post_or_not

router = Router()

@router.message(F.text)
async def handle_links(message: types.Message):
    await message.answer("Staring of link-router")
    
    # if await is_admin(event=message, user_id=message.from_user.id):
    #     return
    
    has_embedded_link = any(e.type == "text_link" for e in message.entities or [])
    has_url_entity = any(e.type == "url" for e in message.entities or [])
    
    if (
        LINK_REGEX.search(message.text) 
        or LOCALHOST_REGEX.search(message.text)
        or has_embedded_link
        or has_url_entity  
    ):
        await message.delete()
        await message.answer(f"{message.from_user.first_name}, скидати посилання в чат заборонено")
        return 
    
    await user_can_post_or_not(message=message)
    
    