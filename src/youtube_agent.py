import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Load .env
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

if not API_KEY:
    raise Exception("YOUTUBE_API_KEY not found")

# Create YouTube client
youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)


def get_trending_videos(region_code="IN", max_results=20):
    """
    Fetch trending YouTube videos.
    """

    try:
        request = youtube.videos().list(
            part="snippet,statistics",
            chart="mostPopular",
            regionCode=region_code,
            maxResults=max_results
        )

        response = request.execute()

        videos = []

        for item in response.get("items", []):
            snippet = item["snippet"]
            stats = item.get("statistics", {})

            videos.append({
                "title": snippet.get("title", ""),
                "channel": snippet.get("channelTitle", ""),
                "published_at": snippet.get("publishedAt", ""),
                "views": int(stats.get("viewCount", 0)),
                "likes": int(stats.get("likeCount", 0)),
                "comments": int(stats.get("commentCount", 0)),
                "video_url": f"https://www.youtube.com/watch?v={item['id']}",
                "thumbnail": snippet["thumbnails"]["high"]["url"]
            })

        return videos

    except HttpError as e:
        print("YouTube API Error:", e)
        return []

    except Exception as e:
        print("Unexpected Error:", e)
        return []


def run_agent():
    """
    Main function called by app.py
    """

    print("=" * 80)
    print("Fetching Trending YouTube Videos")
    print("=" * 80)

    videos = get_trending_videos()

    if not videos:
        print("No videos found.")
        return

    for i, video in enumerate(videos, 1):
        print(f"\n{i}. {video['title']}")
        print(f"Channel   : {video['channel']}")
        print(f"Views     : {video['views']:,}")
        print(f"Likes     : {video['likes']:,}")
        print(f"Comments  : {video['comments']:,}")
        print(f"Published : {video['published_at']}")
        print(f"Video     : {video['video_url']}")
        print("-" * 80)

    return videos


if __name__ == "__main__":
    run_agent()
