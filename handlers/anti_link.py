import asyncio
from handlers.antilink_regex import LINK_REGEX, LOCALHOST_REGEX
from handlers.msg_deleter    import delete_after
from env_collection import TIME_BEFORE_DELETING_WARNING
from texts_to_use   import FORWARDED_FROM_CHANELS_PROHIBITED, LINKS_PROHIBITED
from database       import is_admin
from aiogram        import F, Router, types
from handlers.scaner_advertisement.scaner_of_advetirsment import user_can_post_or_not



router = Router()

@router.message(F.text | F.forward_from_chat | F.caption)
async def handle_links(message: types.Message):
    
    if await is_admin(event=message,user_id=message.from_user.id):
        return
  
    text = message.text or message.caption or ""
    entities = message.entities or message.caption_entities or []

    has_embedded_link = any(e.type == "text_link" for e in entities)
    has_url_entity = any(e.type == "url" for e in entities)

    # Forwarded from channel / chat 
    if message.forward_from_chat:
        await message.delete()
        
        text_of_warning = FORWARDED_FROM_CHANELS_PROHIBITED.format(
                first_name=message.from_user.first_name
                )
        
        warning_ = await message.answer(text_of_warning)
        asyncio.create_task(delete_after(msg=warning_, delay=TIME_BEFORE_DELETING_WARNING))
        return


    if LINK_REGEX.search(text) or LOCALHOST_REGEX.search(text) or has_embedded_link or has_url_entity:
        await message.delete()
        
        text_of_warning = LINKS_PROHIBITED.format(
                first_name=message.from_user.first_name
                )
        
        warning_ = await message.answer(text_of_warning)
        asyncio.create_task(delete_after(msg=warning_, delay=TIME_BEFORE_DELETING_WARNING))
        return
        
    
    if message.text or message.caption:
       await user_can_post_or_not(message=message)
        

