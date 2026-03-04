from fastapi import APIRouter, Query, Request, HTTPException
from app.config import settings
from starlette.responses import PlainTextResponse

router =APIRouter()

@router.get("/webhook")
def verify_webhook(hub_mode: str=Query(alias="hub.mode"),hub_verify_token: str=Query(alias="hub.verify_token"),hub_challenge: str = Query(alias="hub.challenge")):
    if hub_mode=="subscribe" and hub_verify_token==settings.whatsapp_verify_token:
        return PlainTextResponse(hub_challenge)
    else:
        raise HTTPException(status_code=403, detail="Verification Failed")


@router.post("/webhook")
async def receive_webhook(request: Request):
    body=await request.json()
    print(body)
    return {"Stats":200}

