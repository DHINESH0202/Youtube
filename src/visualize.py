import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/youtube_channel_analysis_clean.csv")
sns.set(style="whitegrid")

# Top 10 videos
top10 = df.sort_values("views", ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x="views", y="title", data=top10, palette="viridis")
plt.title("Top 10 Most Viewed Videos")
plt.tight_layout()
plt.show()

# Views over time
plt.figure(figsize=(10,5))
sns.lineplot(x="published_at", y="views", data=df, marker="o")
plt.title("Views over Time")
plt.tight_layout()
plt.show()
