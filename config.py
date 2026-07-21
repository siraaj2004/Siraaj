import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ==========================
# API Keys
# ==========================

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
RESEND_API_KEY = os.getenv("RESEND_API_KEY")

# ==========================
# Email
# ==========================

RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# ==========================
# YouTube Settings
# ==========================

REGION_CODE = "IN"
MAX_RESULTS = 20

# ==========================
# Validation
# ==========================

if not YOUTUBE_API_KEY:
    raise ValueError("YOUTUBE_API_KEY not found in .env")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in .env")

if not RESEND_API_KEY:
    raise ValueError("RESEND_API_KEY not found in .env")

if not RECIPIENT_EMAIL:
    raise ValueError("RECIPIENT_EMAIL not found in .env")
