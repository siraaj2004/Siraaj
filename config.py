import os
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

RESEND_API_KEY = os.getenv("RESEND_API_KEY")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
