import streamlit as st

st.set_page_config(page_title="YouTube Channel Analysis Dashboard", page_icon="📊", layout="wide")

st.markdown("""
<style>
body {
    background-color: #f9fafb;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
h1, h3 {
    color: #334e68;
}
.button-container {
    display: flex;
    justify-content: center;
    gap: 24px;
    margin-top: 2rem;
}
.nav-button {
    background-color: #5a8dee;
    color: white !important;
    border-radius: 12px;
    padding: 16px 48px;
    font-weight: 600;
    font-size: 1.2rem;
    text-decoration: none;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(90, 141, 238, 0.3);
}
.nav-button:hover {
    background-color: #3d6fd1;
    box-shadow: 0 6px 16px rgba(61, 111, 209, 0.4);
}
.info-card {
    margin-top: 40px;
    padding: 24px;
    border-radius: 15px;
    background-color: #ffffff;
    box-shadow: 0 4px 20px rgba(0,0,0,0.07);
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
    color: #57606a;
}
footer {
    margin-top: 3rem;
    text-align: center;
    color: #a0aec0;
    font-size: 0.9rem;
}
</style>

<h1 style="text-align:center;">📊 YouTube Channel Analysis</h1>
<h3 style="text-align:center; font-weight:normal; margin-top:-10px;">Explore & Understand Any Public YouTube Channel</h3>

<div class="info-card">
<p>This app allows you to fetch and analyze data from any public YouTube channel. Get interactive KPIs, charts, and insights delivered with a clean dashboard experience.</p>
</div>

<div class="button-container">
<a href='Home' class="nav-button" target='_self'>🏠 Home</a>
<a href='Analytics' class="nav-button" target='_self'>📈 Analytics</a>
<a href='Video_Comparison' class="nav-button" target='_self'>🎥 Video Comparison</a>
</div>

<footer>Made with ❤️ using Streamlit & Plotly</footer>
""", unsafe_allow_html=True)
