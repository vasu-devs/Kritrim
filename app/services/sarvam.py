from sarvamai import SarvamAI
from io import BytesIO
from app.config import settings

client=SarvamAI(api_subscription_key=settings.sarvam_api_key)

def transcriber(audio_bytes: bytes):
    audio_file=BytesIO(audio_bytes)
    response=client.speech_to_text.transcribe(file=audio_file,model="saaras:v3",mode="transcribe")
    return response.transcript