import pandas as pd
import isodate

df = pd.read_csv("data/youtube_channel_analysis.csv")
df['published_at'] = pd.to_datetime(df['published_at'])
df['duration_s'] = df['duration'].apply(lambda x: isodate.parse_duration(x).total_seconds() if pd.notnull(x) else None)
df['title_len'] = df['title'].str.len()
df['days_since_publish'] = (pd.Timestamp.now(tz=df['published_at'].dt.tz) - df['published_at']).dt.days

df.to_csv("data/youtube_channel_analysis_clean.csv", index=False)
print("✅ Cleaned CSV saved")
