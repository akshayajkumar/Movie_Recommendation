import streamlit as st
import pickle
from recom_functions import recommend_movie, get_high_quality_image

# Load model/data
with open('movie_recommendation.pkl', 'rb') as f:
    file = pickle.load(f)

movie_dict = file['movie_dictionary']
df = file['df']

# --- Custom Styling with Real Blur & Cards ---
st.markdown(
    f"""
    <style>
    /* Background container with blur */
    .blurred-bg {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url("https://plus.unsplash.com/premium_photo-1726848094123-b69f8c83b824?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8bW92aWUlMjBiYWNrZ3JvdW5kfGVufDB8fDB8fHww") no-repeat center center fixed;
        background-size: cover;
        filter: blur(8px) brightness(0.6);  
        z-index: -1;
    }}
    .block-container {{
        position: relative;
        z-index: 1;
        padding: 2rem;
        max-width: 1400px;
        margin: 0 auto;
        color: white;
    }}
    .title {{
        text-align: center;
        font-size: 42px !important;
        color: #facc15;
        font-weight: bold;
        margin-bottom: 20px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
    }}
    .stSelectbox label {{
        color: #facc15 !important;
        font-weight: bold;
        font-size: 18px;
    }}
    /* Card styling */
    .movie-card {{
        background-color: rgba(30, 41, 59, 0.9);
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0px 6px 14px rgba(0,0,0,0.7);
        margin-bottom: 25px;
        text-align: center;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}
    .movie-title {{
        font-size: 20px;
        font-weight: bold;
        color: #38bdf8;
        margin: 10px 0;
        text-align: center;
        text-shadow: 1px 1px 6px black;
    }}
    .movie-details {{
        margin-top: 5px;
        font-size: 15px;
        color: #f1f5f9;
        text-align: center;
    }}
    .chip {{
        display: inline-block;
        background: #334155;
        color: #f1f5f9;
        font-size: 12px;
        padding: 4px 10px;
        border-radius: 20px;
        margin: 2px;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.4);
    }}
    div.stButton > button:first-child {{
        background-color: #e50914;
        color: white !important;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-size: 16px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.6);
    }}
    div.stButton > button:first-child:hover {{
        background-color: #f40612;
        color: white !important;
    }}
    </style>

    <!-- Add blurred background layer -->
    <div class="blurred-bg"></div>
    """,
    unsafe_allow_html=True
)

# --- Title ---
st.markdown("<h1 class='title'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)

# --- Input Selection ---
movie = st.selectbox("📌 Select a movie you like:", movie_dict.keys())
button = st.button("✨ Recommend Similar Movies")

# --- Recommendations ---
if button:
    recommendations = recommend_movie(movie, movie_dict, n=6)

    # Layout: 3 cards per row
    cols = st.columns(3)

    for i, rec in enumerate(recommendations):
        with cols[i % 3]:
            poster_link = df.loc[df['Series_Title'] == rec, 'Poster_Link'].iloc[0]
            link = get_high_quality_image(poster_link, width=250, height=350)

            # Card UI
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.image(link, use_container_width=True)
            st.markdown(f"<p class='movie-title'>{rec}</p>", unsafe_allow_html=True)

            year = df.loc[df['Series_Title'] == rec, 'Released_Year'].iloc[0]
            genre = df.loc[df['Series_Title'] == rec, 'Genre'].iloc[0]
            director = df.loc[df['Series_Title'] == rec, 'Director'].iloc[0]

            st.markdown(f"<p class='movie-details'>📅 Year: <b>{year}</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p class='movie-details'>🎬 Director: <b>{director}</b></p>", unsafe_allow_html=True)

            # Genre as chips (centered)
            chips_html = "".join([f"<span class='chip'>{g.strip()}</span>" for g in genre.split(",")])
            st.markdown(f"<div style='text-align:center; margin-top:10px;'>{chips_html}</div>", unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)
