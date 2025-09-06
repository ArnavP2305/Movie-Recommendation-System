🎬 Movie Recommendation System

A content-based movie recommendation system built with Python, Machine Learning, and Flask, allowing users to get personalized movie suggestions based on their preferences.

Table of Contents

Project Overview

Features

Tech Stack

Installation

Usage

Dataset

Screenshots

Future Improvements

License

Project Overview

This project is a web-based Movie Recommendation System that provides movie suggestions to users based on a selected movie. The system uses cosine similarity to find movies with similar descriptions, genres, and other metadata.

It demonstrates practical applications of Natural Language Processing (NLP), Vectorization, and Machine Learning in recommendation systems.

Features

User-friendly Flask web interface

Enter a movie and get recommended movies instantly

Content-based filtering using TF-IDF / Count Vectorization

Recommendations based on movie descriptions and metadata

Works offline using a pre-trained model

Tech Stack

Python – Programming language

Flask – Web framework

Pandas & NumPy – Data manipulation

Scikit-learn – Machine learning & similarity calculations

HTML/CSS – Frontend interface

Pickle – Saving trained model

Installation

Clone the repository:

git clone https://github.com/ArnavP2305/Movie-Recommendation-System.git
cd Movie-Recommendation-System


Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows


Install dependencies:

pip install -r requirements.txt

Usage

Run the Flask app:

python app.py


Open your browser and go to:

http://127.0.0.1:5000


Enter a movie name and get top 5 recommended movies.

Dataset

Dataset used: Movie metadata from Kaggle or any publicly available movie dataset.

Includes movie titles, descriptions, genres, and other metadata.


Future Improvements

Add user login and personalized recommendations

Add collaborative filtering for hybrid recommendations

Improve UI with Bootstrap or React.js

License

This project is open-source and available under the MIT License.
