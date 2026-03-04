from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    whatsapp_verify_token: str
    whatsapp_api_token: str
    whatsapp_phone_number_id: str

    class Config:
        env_file=".env"
settings=Settings()