📊 YouTube Channel Analysis Dashboard
An interactive Streamlit app to analyze any public YouTube channel using the YouTube Data API v3.
Fetch video data, explore analytics, compare videos, and get insights in a beautiful dashboard.

🚀 Features
Fetch latest videos from any public YouTube channel

KPI metrics: views, likes, engagement

Top 10 videos chart

Trends: views over time, likes vs comments scatter plot

Download filtered video data as CSV

Compare videos side-by-side (Video Comparison Tool)

Modern UI with soft colors and clean alignment

Secure API access using environment variables (not stored in repo)

🛠️ Tech Stack
Streamlit (dashboard & UI)

YouTube Data API v3

pandas (data handling)

Plotly (charting)

python-dotenv (local secrets)

Streamlit Cloud (deployment)

📂 Directory Structure
kotlin
Copy code
Youtube/
├── app.py
├── pages/
│   ├── 1_Home.py
│   ├── 2_Analytics.py
│   ├── 3_Video_Comparison.py
├── data/
├── requirements.txt
├── .gitignore
├── README.md
⚙️ How to Run Locally
bash
Copy code
git clone https://github.com/dhinesh0202/Youtube.git
cd Youtube

python -m venv venv          # optional, recommended
# Activate the virtual environment
# Mac/Linux:
source venv/bin/activate     
# Windows:
venv\Scripts\activate        

pip install -r requirements.txt

# Create your .env file (do NOT commit!)
echo "YT_API_KEY=your_actual_youtube_api_key" > .env

streamlit run app.py
🌐 Deploy on Streamlit Cloud
Push your code to GitHub (exclude .env file!).

Go to streamlit.io/cloud

Click New App → choose your repo, branch (main), and file (app.py)

In Secrets, add:

ini
Copy code
YT_API_KEY = "your_actual_youtube_api_key"
Click Deploy. Share your app link!

🤝 Contribution
Contributions are welcome!
Fork the repo, create a branch, and open a pull request.

📜 License
MIT License

👤 Author
Dhinesh
GitHub: @dhinesh0202
Live App: dhinesh-youtube-dashboard.streamlit.app
