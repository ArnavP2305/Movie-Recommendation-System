from flask import Flask, render_template, request
import pickle
import pandas as pd
import requests
import os
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# =========================
# Load saved model artifacts
# =========================
with open("movie_recommender.pkl", "rb") as f:
    artifacts = pickle.load(f)

df = artifacts["movies"]
cv = artifacts["vectorizer"]

# =========================
# Compute similarity matrix
# =========================
count_matrix = cv.transform(df['title'])
cosine_sim = cosine_similarity(count_matrix)

# =========================
# OMDB API KEY (from Render env)
# =========================
OMDB_API_KEY = os.environ.get("OMDB_API_KEY")



# =========================
# Fetch movie poster
# =========================
def get_poster(title):
    try:
        url = f"https://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
        response = requests.get(url, timeout=5).json()

        if response.get("Poster") and response["Poster"] != "N/A":
            return response["Poster"]
    except:
        pass

    return "https://via.placeholder.com/300x450?text=No+Image"

# =========================
# Recommendation function
# =========================
def recommend(movie_name, df, cosine_sim):
    # Case-insensitive exact match
    matches = df[df['title'].str.lower() == movie_name.lower()]

    # Partial match if exact not found
    if matches.empty:
        matches = df[df['title'].str.contains(movie_name, case=False, na=False)]

    if matches.empty:
        return [], []

    idx = matches.index[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Top 10 recommendations

    movie_indices = [i[0] for i in sim_scores]
    recommendations = df['title'].iloc[movie_indices].tolist()

    posters = [get_poster(title) for title in recommendations]

    return recommendations, posters

# =========================
# Flask Routes
# =========================
@app.route("/", methods=["GET", "POST"])
def index():
    movie_data = []

    if request.method == "POST":
        movie_name = request.form.get("movie_name")
        recommendations, posters = recommend(movie_name, df, cosine_sim)
        movie_data = list(zip(recommendations, posters))

    return render_template("index.html", movie_data=movie_data)

# =========================
# Render Deployment Entry
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)