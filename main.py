import os
from googleapiclient.discovery import build
import pandas as pd
from dotenv import load_dotenv
import isodate

# Load API key
load_dotenv()
API_KEY = os.getenv("YT_API_KEY")
CHANNEL_ID = "UCJcCB-QYPIBcbKcBQOTwhiA"  # Example channel
LIMIT_VIDEOS = 100

if not API_KEY:
    raise ValueError("❌ API key not found in .env")

youtube = build("youtube", "v3", developerKey=API_KEY)

# Get uploads playlist
res = youtube.channels().list(part="contentDetails", id=CHANNEL_ID).execute()
uploads_playlist = res["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

# Fetch video IDs
videos = []
next_page = None
while True and len(videos) < LIMIT_VIDEOS:
    pl = youtube.playlistItems().list(
        part="snippet",
        playlistId=uploads_playlist,
        maxResults=50,
        pageToken=next_page
    ).execute()

    for item in pl["items"]:
        videos.append(item["snippet"]["resourceId"]["videoId"])
        if len(videos) >= LIMIT_VIDEOS:
            break
    next_page = pl.get("nextPageToken")
    if not next_page:
        break

# Fetch video details
rows = []
for i in range(0, len(videos), 50):
    ids = ",".join(videos[i:i+50])
    details = youtube.videos().list(part="snippet,statistics,contentDetails", id=ids).execute()
    for v in details["items"]:
        snip = v["snippet"]
        stats = v.get("statistics", {})
        cd = v.get("contentDetails", {})
        rows.append({
            "video_id": v["id"],
            "title": snip.get("title"),
            "published_at": snip.get("publishedAt"),
            "duration": cd.get("duration"),
            "views": int(stats.get("viewCount", 0)),
            "likes": int(stats.get("likeCount", 0)) if stats.get("likeCount") else 0,
            "comments": int(stats.get("commentCount", 0)) if stats.get("commentCount") else 0
        })

df = pd.DataFrame(rows)
os.makedirs("data", exist_ok=True)
df.to_csv("data/youtube_channel_analysis.csv", index=False)
print(f"✅ Saved CSV with {len(df)} videos")
