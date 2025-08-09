📊 YouTube Channel Analysis Dashboard
Analyze any public YouTube channel with this interactive Streamlit app using the YouTube Data API v3.
Fetch video data, explore key metrics, visualize trends, and compare videos — all in a sleek dashboard.

🚀 Features
Fetch latest videos from any public YouTube channel

Key metrics: views, likes, engagement rate

Visualize top videos with interactive charts

Trend analysis: views over time, likes vs comments

Download filtered data as CSV for further analysis

Compare videos side-by-side

Clean, intuitive UI with secure API key handling

🛠️ Tech Stack
Streamlit for UI and dashboard

YouTube Data API v3 for data fetching

pandas for data processing

Plotly for interactive visualizations

python-dotenv for environment variables

⚙️ Run Locally
bash
Copy
Edit
git clone https://github.com/dhinesh0202/Youtube.git
cd Youtube

python -m venv venv
# Activate virtual environment:
# Mac/Linux: source venv/bin/activate
# Windows: venv\Scripts\activate

pip install -r requirements.txt

echo "YT_API_KEY=your_youtube_api_key" > .env

streamlit run app.py
🌐 Deploy on Streamlit Cloud
Push your code to GitHub (exclude .env)

On Streamlit Cloud, create a new app pointing to your repo and app.py

Add your API key as a secret (YT_API_KEY)

Deploy and share your app!

👤 Author
Dhinesh
GitHub: https://github.com/dhinesh0202

