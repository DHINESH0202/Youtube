import os
import pandas as pd
import streamlit as st
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("YT_API_KEY")

st.markdown("""
<style>
.kpi-card {
    background-color: #e7f0fc;
    border-radius: 14px;
    padding: 20px;
    box-shadow: 0 3px 15px rgba(78, 115, 181, 0.2);
    text-align: center;
    color: #2c3e50;
}
.kpi-value {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 4px;
}
.kpi-label {
    font-weight: 600;
    font-size: 1rem;
    color: #4d688c;
}
</style>
""", unsafe_allow_html=True)

def fetch_youtube_data(api_key, channel_id, limit=50):
    youtube = build("youtube", "v3", developerKey=api_key)
    uploads_playlist = youtube.channels().list(part="contentDetails", id=channel_id).execute()["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    video_ids, next_page = [], None
    while len(video_ids) < limit:
        pl = youtube.playlistItems().list(part="snippet", playlistId=uploads_playlist, maxResults=50, pageToken=next_page).execute()
        for item in pl["items"]:
            video_ids.append(item["snippet"]["resourceId"]["videoId"])
            if len(video_ids) >= limit:
                break
        next_page = pl.get("nextPageToken")
        if not next_page:
            break

    rows = []
    for i in range(0, len(video_ids), 50):
        ids = ",".join(video_ids[i:i+50])
        vids = youtube.videos().list(part="snippet,statistics", id=ids).execute()
        for v in vids["items"]:
            snip, stats = v["snippet"], v.get("statistics", {})
            rows.append({
                "video_id": v["id"],
                "title": snip.get("title"),
                "published_at": snip.get("publishedAt"),
                "views": int(stats.get("viewCount", 0)),
                "likes": int(stats.get("likeCount", 0)) if stats.get("likeCount") else 0,
                "comments": int(stats.get("commentCount", 0)) if stats.get("commentCount") else 0
            })
    return pd.DataFrame(rows)

st.markdown("## 🏠 Home · Fetch Channel Videos")

if not API_KEY:
    st.error("❌ API Key missing! Please set YT_API_KEY in your .env")
else:
    col1, col2 = st.columns([4,1])
    with col1:
        channel_id = st.text_input("Enter YouTube Channel ID", "UCY6KjrDBN_tIRFT_QNqQbRQ", 
                                   help="Paste the channel ID (starts with 'UC...')")
    with col2:
        limit = st.slider("Number of Videos to Fetch", 10, 100, 50, step=10)

    if st.button("🔄 Fetch Data"):
        with st.spinner("Fetching data..."):
            df = fetch_youtube_data(API_KEY, channel_id, limit)
            os.makedirs("data", exist_ok=True)
            cache_path = f"data/{channel_id}_videos.csv"
            df.to_csv(cache_path, index=False)
            st.success(f"✅ Fetched {len(df):,} videos. Saved to cache.")

            k1,k2,k3 = st.columns(3)
            k1.markdown(f"<div class='kpi-card'><div class='kpi-value'>{len(df):,}</div><div class='kpi-label'>Videos</div></div>", unsafe_allow_html=True)
            k2.markdown(f"<div class='kpi-card'><div class='kpi-value'>{df['views'].sum():,}</div><div class='kpi-label'>Total Views</div></div>", unsafe_allow_html=True)
            k3.markdown(f"<div class='kpi-card'><div class='kpi-value'>{df['likes'].sum():,}</div><div class='kpi-label'>Total Likes</div></div>", unsafe_allow_html=True)

            st.dataframe(df, height=450)
    else:
        st.info("Enter a channel ID and click 'Fetch Data' to start.")
