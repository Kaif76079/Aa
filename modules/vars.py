import os

API_ID    = os.environ.get("API_ID", "22471119")
API_HASH  = os.environ.get("API_HASH", "b8ab98fab8020ad7eab4c38f1ec9e1ae")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8159648223:AAFP3Cxj863pdJuPkmjdJDmEA2ud65RYJUY") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
