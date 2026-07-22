import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load .env
ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")


def check_env():
    required = [
        "YOUTUBE_API_KEY",
        "RECIPIENT_EMAIL"
    ]

    missing = []

    for key in required:
        if not os.getenv(key):
            missing.append(key)

    if missing:
        print("❌ Missing environment variables:")
        for key in missing:
            print(f" - {key}")
        sys.exit(1)

    print("✅ Environment variables loaded successfully.")


def main():
    check_env()

    try:
        import youtube_agent
    except Exception as e:
        print(f"❌ Failed to import youtube_agent: {e}")
        sys.exit(1)

    if not hasattr(youtube_agent, "run_agent"):
        print("❌ run_agent() function not found in youtube_agent.py")
        print("Available functions:")
        print(dir(youtube_agent))
        sys.exit(1)

    try:
        youtube_agent.run_agent()
        print("✅ YouTube agent completed successfully.")
    except Exception as e:
        print(f"❌ Runtime Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
