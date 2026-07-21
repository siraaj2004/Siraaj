import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load .env
ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

# Environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")


def check_env():
    required = {
        "OPENROUTER_API_KEY": OPENROUTER_API_KEY,
        "RESEND_API_KEY": RESEND_API_KEY,
        "YOUTUBE_API_KEY": YOUTUBE_API_KEY,
        "RECIPIENT_EMAIL": RECIPIENT_EMAIL,
    }

    missing = [key for key, value in required.items() if not value]

    if missing:
        print("❌ Missing environment variables:")
        for item in missing:
            print(f"   - {item}")
        sys.exit(1)

    print("✅ Environment variables loaded successfully.")


def main():
    check_env()

    try:
        from youtube_agent import run_agent
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        sys.exit(1)

    try:
        run_agent()
        print("✅ Agent finished successfully.")
    except Exception as e:
        print(f"❌ Agent Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
