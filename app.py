from flask import Flask, render_template, request
import pickle
import pandas as pd
import requests
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load saved artifacts
with open("movie_recommender.pkl", "rb") as f:
    artifacts = pickle.load(f)

df = artifacts["movies"]
cv = artifacts["vectorizer"]

# Compute similarity matrix on the fly
count_matrix = cv.transform(df['title'])
cosine_sim = cosine_similarity(count_matrix)

# Your OMDB API key
OMDB_API_KEY = "573c6225"

def get_poster(title):
    """Fetch poster from OMDB API"""
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url).json()
    if "Poster" in response and response["Poster"] != "N/A":
        return response["Poster"]
    return "https://via.placeholder.com/300x450?text=No+Image"

def recommend(movie_name, df, cosine_sim):
    # Case-insensitive exact match
    matches = df[df['title'].str.lower() == movie_name.lower()]

    # If no exact match, try partial match
    if matches.empty:
        matches = df[df['title'].str.contains(movie_name, case=False, na=False)]

    if matches.empty:
        return [], []

    idx = matches.index[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Top 10

    movie_indices = [i[0] for i in sim_scores]
    recommendations = df['title'].iloc[movie_indices].tolist()

    posters = [get_poster(title) for title in recommendations]

    return recommendations, posters


@app.route("/", methods=["GET", "POST"])
def index():
    movie_data = []
    if request.method == "POST":
        movie_name = request.form["movie_name"]
        recommendations, posters = recommend(movie_name, df, cosine_sim)
        movie_data = list(zip(recommendations, posters))

    return render_template("index.html", movie_data=movie_data)


if __name__ == "__main__":
    app.run(debug=True)
