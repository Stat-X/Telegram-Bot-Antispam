import asyncio

async def delete_after(msg, delay=10):
    await asyncio.sleep(delay)
    try:
        await msg.delete()
    except Exception:
        pass