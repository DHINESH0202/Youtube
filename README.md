📊 YouTube Channel Analysis Dashboard
Analyze any public YouTube channel with an interactive Streamlit app using the YouTube Data API v3.
Fetch video data, explore analytics, compare videos, and visualize key metrics in a sleek dashboard.

🚀 Features
Fetch latest videos from any public YouTube channel

Key metrics: views, likes, engagement

Top 10 videos chart

Trends: views over time, likes vs comments scatter plot

Download filtered video data as CSV

Compare videos side-by-side

Modern UI with secure API key handling

🛠️ Tech Stack
Streamlit (UI & dashboard)

YouTube Data API v3

pandas (data handling)

Plotly (charts)

python-dotenv (env variables)

📂 Project Structure
Copy
Edit
Youtube/
├── app.py
├── pages/
│   ├── 1_Home.py
│   ├── 2_Analytics.py
│   ├── 3_Video_Comparison.py
├── requirements.txt
├── .gitignore
├── README.md
⚙️ Running Locally
bash
Copy
Edit
git clone https://github.com/dhinesh0202/Youtube.git
cd Youtube

python -m venv venv
# Activate:
# Mac/Linux: source venv/bin/activate
# Windows: venv\Scripts\activate

pip install -r requirements.txt

echo "YT_API_KEY=your_actual_youtube_api_key" > .env

streamlit run app.py
🌐 Deploy on Streamlit Cloud
Push code to GitHub (exclude .env)

Create new app on streamlit.io/cloud

Set secret YT_API_KEY with your API key

Deploy and share your app

👤 Author
Dhinesh
GitHub | Live Demo

