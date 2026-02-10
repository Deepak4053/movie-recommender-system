# 🎬 Movie Recommender System

A content-based movie recommendation system built using **Python, Streamlit, and Machine Learning**.

This application suggests similar movies based on a selected movie using a precomputed similarity matrix and real-time data from the TMDB API.

---

## 🚀 Features

- 🔎 Search for a movie
- 🎥 View selected movie details
- ⭐ Display movie ratings
- 🎭 Show movie genres
- 🍿 Get Top 5 similar movie recommendations
- ⚡ Fast recommendations using precomputed similarity matrix
- 🌐 Real-time movie data from TMDB API
- 🖥️ Clean and responsive UI

---

## 🧠 How It Works

This project uses a **content-based filtering approach**:

1. Movie metadata (overview, genres, keywords, cast, etc.) is combined.
2. Text vectorization is applied using `CountVectorizer` / `TF-IDF`.
3. Cosine similarity is calculated between movie vectors.
4. A similarity matrix is precomputed and stored.
5. When a user selects a movie, the system retrieves the top 5 most similar movies.

---

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Requests
- TMDB API


## 📂 Project Structure

