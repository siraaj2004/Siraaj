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
        "RECIPIENT_EMAIL",
        "RESEND_API_KEY"
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
        from sender import send_email
    except Exception as e:
        print(f"❌ Import Error: {e}")
        sys.exit(1)

    try:
        print("📺 Fetching YouTube trending videos...")

        videos = youtube_agent.run_agent()

        print(f"✅ Retrieved {len(videos)} videos.")

        body = "🔥 YouTube Trending Videos\n\n"

        for i, video in enumerate(videos, start=1):
            body += (
                f"{i}. {video['title']}\n"
                f"Channel : {video['channel']}\n"
                f"Views   : {video['views']:,}\n"
                f"Likes   : {video['likes']:,}\n"
                f"Comments: {video['comments']:,}\n"
                f"URL     : {video['video_url']}\n\n"
            )

        print("📧 Sending email...")

        send_email(
            subject="🔥 YouTube Trending Videos",
            body=body
        )

        print("✅ Workflow completed successfully.")

    except Exception as e:
        print(f"❌ Runtime Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
