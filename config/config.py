import os
from dotenv import load_dotenv

load_dotenv(override=True)

NGROK_DOMAIN = os.getenv("NGROK_DOMAIN")
NGROK_AUTHTOKEN = os.getenv("NGROK_AUTHTOKEN")
PUBLIC_PORT = os.getenv("PUBLIC_PORT")
BASE_URL = os.getenv("BASE_URL")
LM_STUDIO_PORT = os.getenv("LM_STUDIO_PORT")