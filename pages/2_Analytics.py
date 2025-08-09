import os
import pandas as pd
import streamlit as st
import plotly.express as px

# ===== Helper function =====
def enrich(df):
    df['published_at'] = pd.to_datetime(df['published_at'])
    df['engagement_rate'] = ((df['likes'] + df['comments']) / df['views']).fillna(0)
    df['weekday'] = df['published_at'].dt.strftime('%A')
    return df

# ===== Page Title =====
st.markdown("## 📈 Analytics · Insights Overview")

# ===== Load Data =====
data_files = [f for f in os.listdir("data") if f.endswith(".csv")]

if not data_files:
    st.warning("No cached video data found. Please fetch data on the Home page first.")
else:
    file_choice = st.selectbox("📂 Select Cached Channel Data", data_files)
    df = pd.read_csv(os.path.join("data", file_choice))
    df = enrich(df)

    # ===== Sidebar Filters =====
    st.sidebar.header("🔍 Filters")
    min_view = st.sidebar.slider(
        "Minimum Views",
        int(df['views'].min()),
        int(df['views'].max()),
        int(df['views'].min())
    )
    search_title = st.sidebar.text_input("Search Video Title")

    filtered = df[df['views'] >= min_view]
    if search_title:
        filtered = filtered[filtered['title'].str.contains(search_title, case=False, na=False)]

    # ===== KPI Cards =====
    st.markdown("""
        <style>
        .kpi-card {
            border-radius: 12px;
            padding: 18px;
            background: #f2f7ff;
            color: #2a374d;
            text-align: center;
            margin-bottom: 20px;
            box-shadow: 0 3px 10px rgba(22, 73, 141, 0.12);
        }
        .kpi-value {
            font-size: 2rem;
            font-weight: 700;
        }
        .kpi-label {
            font-size: 1rem;
            opacity: 0.8;
            margin-top: 4px;
        }
        </style>
    """, unsafe_allow_html=True)

    kpi_cols = st.columns(4)
    kpi_cols[0].markdown(f"<div class='kpi-card'><div class='kpi-value'>{len(filtered):,}</div><div class='kpi-label'>Videos</div></div>", unsafe_allow_html=True)
    kpi_cols[1].markdown(f"<div class='kpi-card'><div class='kpi-value'>{filtered['views'].sum():,}</div><div class='kpi-label'>Total Views</div></div>", unsafe_allow_html=True)
    kpi_cols[2].markdown(f"<div class='kpi-card'><div class='kpi-value'>{filtered['likes'].sum():,}</div><div class='kpi-label'>Total Likes</div></div>", unsafe_allow_html=True)
    kpi_cols[3].markdown(f"<div class='kpi-card'><div class='kpi-value'>{(filtered['engagement_rate'].mean()*100):.1f}%</div><div class='kpi-label'>Avg Engagement</div></div>", unsafe_allow_html=True)

    st.markdown("---")

    # ===== Tabs Layout =====
    tab1, tab2 = st.tabs(["🏆 Top 10 Videos", "📊 Trends"])

    # ---------- TAB 1: Top Videos ----------
    with tab1:
        st.markdown("### 🏆 Top 10 Videos by Views")
        top10 = filtered.sort_values('views', ascending=False).head(10)
        fig = px.bar(
            top10,
            x='views',
            y='title',
            orientation='h',
            color='views',
            color_continuous_scale='Blues',
            hover_data=['likes', 'comments', 'engagement_rate']
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("#### 📋 Video Details")
        st.dataframe(
            top10[['title', 'views', 'likes', 'comments', 'engagement_rate', 'published_at']],
            height=280
        )

    # ---------- TAB 2: Trends ----------
    with tab2:
        st.markdown("### 📈 Views Over Time")
        fig_line = px.line(
            filtered.sort_values("published_at"),
            x="published_at",
            y="views",
            markers=True,
            hover_data=["title"]
        )
        st.plotly_chart(fig_line, use_container_width=True)

        st.markdown("### 💬 Likes vs Comments")
        fig_scatter = px.scatter(
            filtered,
            x='likes',
            y='comments',
            size='views',
            color='views',
            color_continuous_scale='Viridis',
            hover_data=['title']
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    # ===== Download =====
    st.markdown("---")
    st.download_button(
        "💾 Download Filtered Data CSV",
        filtered.to_csv(index=False),
        "filtered_data.csv",
        "text/csv"
    )
