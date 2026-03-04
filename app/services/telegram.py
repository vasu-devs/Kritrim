from app.config import settings
import httpx

async def send_message(chat_id: int , text: str):
    url=f"https://api.telegram.org/bot{settings.telegram_bot_token}/sendMessage"
    async with httpx.AsyncClient() as client:
        response=await client.post(url,json={"chat_id": chat_id, "text":text})
    
async def download_voice(file_id: str):
    url=f"https://api.telegram.org/bot{settings.telegram_bot_token}/getFile?file_id={file_id}"
    async with httpx.AsyncClient() as client:
        response1 = await client.get(url)

        body=response1.json()
        file_path=body["result"]["file_path"]
        
        response2 = await client.get(f"https://api.telegram.org/file/bot{settings.telegram_bot_token}/{file_path}")

        return response2.content