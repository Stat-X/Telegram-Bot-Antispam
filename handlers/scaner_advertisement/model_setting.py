import os
from openai import OpenAI
from dotenv import load_dotenv
import asyncio

load_dotenv()

API_KEY=os.getenv("API_OPEN_AI")

client = OpenAI(api_key=API_KEY)


async def is_advertisement(text: str) -> bool:
    
    prompt = f"""
    You are a moderator in a chat.

Your task is to detect whether the message is a REAL commercial advertisement.

Classify the message as 1 ONLY if it clearly contains at least one of the following:
- An offer to sell, buy, rent, promote, or advertise goods or services.
- A business or commercial proposal.
- A price, quantity, delivery terms, payment terms, or a call to contact for business.
- Contact information (phone, email, website, Telegram, WhatsApp, etc.) together with a commercial offer.
- Phrases like: "for sale", "selling", "buy", "we offer", "available", "order now", "delivery", "wholesale", "retail", "price", "discount", "contact us", etc.

Classify the message as 0 if:
- It is a greeting, casual conversation, or personal message.
- It is a question, discussion, or opinion without a commercial intent.
- It is news, announcements, or information not trying to sell or promote something.
- It is spam, jokes, or unrelated text with no business intent.

Important:
- The presence of a product name alone is NOT enough to be an advertisement.
- The presence of a phone number or link alone is NOT enough — it must be tied to a commercial offer.
- Classify as 1 ONLY when there is a clear commercial intent.


Output ONLY one digit: 1 or 0.

    Text:
    {text}
    """
    
    loop = asyncio.get_running_loop()
    response = await loop.run_in_executor(
        None,
        lambda: client.responses.create(
            model="gpt-5-nano",
            input=prompt
        )
    )
    return bool(int(response.output_text.strip()))



