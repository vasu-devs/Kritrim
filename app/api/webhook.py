from fastapi import APIRouter , Request 
from app.config import settings
from app.services.telegram import send_message

router=APIRouter()

@router.post("/webhook")
async def receive_webhook(request: Request):
    body=await request.json()
    message=body.get("message")
    if message:
        chat_id=message["chat"]["id"]
        text=message.get("text")
        if text:
            await send_message(chat_id,f"You said: {text}")
        print(chat_id, "\n" , text)
    return {"status":"ok"}