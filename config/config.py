import os
from dotenv import load_dotenv

load_dotenv(override=True)

NGROK_DOMAIN = os.getenv("NGROK_DOMAIN")
NGROK_AUTHTOKEN = os.getenv("NGROK_AUTHTOKEN")