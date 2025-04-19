# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Python and Machine Learning. It suggests movies similar to the user's input using cosine similarity on movie features such as genres, cast, director, and keywords.

---

## 📌 Features

- Recommends similar movies based on a selected movie title
- Uses cosine similarity to find similarity between movies
- Built using popular Python libraries: Pandas, Scikit-learn, and Numpy
- Easy-to-use interface (optional: can be integrated with a web app using Flask or Streamlit)

---

## 🛠️ Tech Stack

- **Python**
- **Pandas** – Data manipulation
- **Scikit-learn** – Feature extraction and similarity calculation
- **Numpy** – Numerical operations
- **Jupyter Notebook** – For prototyping and testing
- *(Optional)* Flask/Streamlit – For deploying a simple web app

---

## 📊 Dataset

- **TMDB 5000 Movie Dataset**
- Contains metadata like: `title`, `genres`, `cast`, `crew`, `keywords`, `overview`, etc.
- Source: [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

## 🚀 How It Works

1. Combine important features into a single string (e.g., genres, cast, director, keywords)
2. Convert the text data into numerical vectors using `CountVectorizer`
3. Compute similarity score using **cosine similarity**
4. Recommend top N movies based on similarity to the input movie

---

## 🧠 How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/movie-recommender.git
   cd movie-recommender


