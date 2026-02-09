import streamlit as st
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# -----------------------------
# Custom CSS Styling
# -----------------------------
st.markdown("""
    <style>
    .main-title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #E50914;
    }
    .movie-title {
        font-size: 18px;
        font-weight: bold;
        text-align: center;
    }
    .rating {
        text-align: center;
        color: gold;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🎬 Movie Recommender System</p>', unsafe_allow_html=True)
st.write("Discover movies similar to your favorites.")

# -----------------------------
# Load Data
# -----------------------------
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# -----------------------------
# Fetch Movie Details
# -----------------------------
def fetch_movie_details(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        data = requests.get(url).json()

        poster_path = data.get("poster_path")
        overview = data.get("overview")
        rating = data.get("vote_average")

        poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else None

        return poster_url, overview, rating

    except:
        return None, "No description available.", "N/A"

# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        poster, overview, rating = fetch_movie_details(movie_id)

        recommended_movies.append({
            "title": title,
            "poster": poster,
            "overview": overview,
            "rating": rating
        })

    return recommended_movies


# -----------------------------
# Movie Selection
# -----------------------------
selected_movie = st.selectbox(
    "Choose a movie",
    movies['title'].values
)

# -----------------------------
# Recommend Button
# -----------------------------
if st.button("Recommend Movies"):

    with st.spinner("Finding similar movies..."):
        recommendations = recommend(selected_movie)

    cols = st.columns(5)

    for col, movie in zip(cols, recommendations):
        with col:
            if movie["poster"]:
                st.image(movie["poster"])
            st.markdown(f"<p class='movie-title'>{movie['title']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='rating'>⭐ {movie['rating']}</p>", unsafe_allow_html=True)
            st.caption(movie["overview"][:150] + "...")
