import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

if not YOUTUBE_API_KEY:
    raise ValueError("YOUTUBE_API_KEY not found in .env")

youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)


def get_latest_videos(
    query="Telugu movies",
    max_results=10,
    region_code="IN"
):
    """
    Search latest YouTube videos by keyword.
    No RSS.
    No Channel ID.
    """

    search_response = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        order="date",
        regionCode=region_code,
        maxResults=max_results
    ).execute()

    videos = []

    video_ids = [
        item["id"]["videoId"]
        for item in search_response["items"]
    ]

    if not video_ids:
        return []

    stats_response = youtube.videos().list(
        part="statistics",
        id=",".join(video_ids)
    ).execute()

    stats = {
        item["id"]: item["statistics"]
        for item in stats_response["items"]
    }

    for item in search_response["items"]:
        video_id = item["id"]["videoId"]

        video = {
            "title": item["snippet"]["title"],
            "channel": item["snippet"]["channelTitle"],
            "published": item["snippet"]["publishedAt"],
            "video_url": f"https://www.youtube.com/watch?v={video_id}",
            "views": stats.get(video_id, {}).get("viewCount", "0"),
            "likes": stats.get(video_id, {}).get("likeCount", "0"),
            "comments": stats.get(video_id, {}).get("commentCount", "0")
        }

        videos.append(video)

    return videos


if __name__ == "__main__":

    keywords = [
        "Telugu movies",
        "Telugu thriller",
        "Telugu comedy",
        "AI",
        "Technology"
    ]

    for keyword in keywords:

        print("=" * 80)
        print("Keyword:", keyword)
        print("=" * 80)

        videos = get_latest_videos(keyword)

        for i, video in enumerate(videos, start=1):
            print(f"{i}. {video['title']}")
            print("Channel :", video["channel"])
            print("Views   :", video["views"])
            print("Likes   :", video["likes"])
            print("Comments:", video["comments"])
            print("Published:", video["published"])
            print(video["video_url"])
            print("-" * 80)
