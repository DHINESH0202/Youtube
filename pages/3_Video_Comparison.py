import os
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

def enrich(df):
    df['published_at'] = pd.to_datetime(df['published_at'])
    df['engagement_rate'] = ((df['likes'] + df['comments']) / df['views']).fillna(0)
    return df

st.markdown("## 🎥 Video Comparison Tool")

data_files = [f for f in os.listdir("data") if f.endswith(".csv")]
if not data_files:
    st.warning("No data found. Please fetch channel data on the Home page first.")
else:
    file_choice = st.selectbox("Select Channel Data File", data_files)
    df = pd.read_csv(os.path.join("data", file_choice))
    df = enrich(df)

    video_titles = df['title'].tolist()
    selected_videos = st.multiselect(
        "Select videos to compare (2-5 videos)",
        options=video_titles,
        default=video_titles[:2],
        max_selections=5
    )

    if len(selected_videos) < 2:
        st.info("Please select at least two videos for comparison.")
    else:
        comp_df = df[df['title'].isin(selected_videos)].copy()
        comp_df = comp_df.set_index('title')

        st.markdown("### 📊 Comparison Table")
        st.dataframe(comp_df[['views', 'likes', 'comments', 'engagement_rate', 'published_at']].sort_values('views', ascending=False))

        categories = ['Views', 'Likes', 'Comments', 'Engagement Rate']
        radar_df = {
            'Views': comp_df['views'],
            'Likes': comp_df['likes'],
            'Comments': comp_df['comments'],
            'Engagement Rate': comp_df['engagement_rate'] * 100
        }

        fig = go.Figure()
        max_vals = {
            'Views': df['views'].max(),
            'Likes': df['likes'].max(),
            'Comments': df['comments'].max(),
            'Engagement Rate': 100
        }

        for title in comp_df.index:
            fig.add_trace(go.Scatterpolar(
                r=[radar_df[cat][title] / max_vals[cat] * 100 for cat in categories],
                theta=categories,
                fill='toself',
                name=title
            ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0,100]
                )
            ),
            showlegend=True,
            title="Normalized Performance Radar Chart"
        )

        st.plotly_chart(fig, use_container_width=True)
