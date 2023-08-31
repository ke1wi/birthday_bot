import os 

class Settings:
    
    TOKEN: str = os.getenv("TOKEN")
    CHANNEL_URL: str = os.getenv("CHANNEL_URL")
    CHAT_ID: int = int(os.getenv("CHAT_ID"))
    ADMIN_ID: str = os.getenv("ADMIN_ID")