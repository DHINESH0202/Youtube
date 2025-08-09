📊 YouTube Channel Analysis Dashboard
Analyze any public YouTube channel with this interactive Streamlit app using the YouTube Data API v3.
Fetch video data, explore key metrics, visualize trends, and compare videos — all in a sleek, user-friendly dashboard.

🌐 Try the Demo
Explore the live app here:
👉 https://dhinesh-youtube-dashboard.streamlit.app

⚙️ How to Run Locally
bash
Copy
Edit
git clone https://github.com/dhinesh0202/Youtube.git
cd Youtube

python -m venv venv
# Activate virtual environment:
# Mac/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

pip install -r requirements.txt

echo "YT_API_KEY=your_youtube_api_key" > .env

streamlit run app.py

☁️ Deploy on Streamlit Cloud
Push your code to GitHub (do NOT commit .env)

Create a new app on Streamlit Cloud pointing to your repo and app.py

Add your API key as a secret with the key name YT_API_KEY

Deploy and share your app with others!

👤 Author
Dhinesh
GitHub: https://github.com/dhinesh0202
