from fastapi import APIRouter , Request 
from app.config import settings
from app.services.telegram import send_message, download_voice
from app.services.sarvam import transcriber

router=APIRouter()

@router.post("/webhook")
async def receive_webhook(request: Request):
    body=await request.json()
    message=body.get("message")
    if message:
        chat_id=message["chat"]["id"]

        if message.get("voice"):
            file_id=message["voice"]["file_id"]
            audio_bytes=await download_voice(file_id)
            transcript=transcriber(audio_bytes)
            await send_message(chat_id,f"You said: {transcript}")

        elif message.get("text"):
            text=message.get("text")
            await send_message(chat_id,f"You said: {text}")

    return {"status":"ok"}