# 🎬 Movie Recommendation System

## 📌 Project Overview
This project is a **Movie Recommendation System** built using **content-based filtering**.  
It suggests movies similar to the one selected by the user, based on cosine similarity of feature vectors.  
The system is deployed with **Streamlit** and uses the **IMDb Top 1000 dataset**.

---

## ⚙️ Tech Stack
- **Python** 🐍  
- **Libraries**: Streamlit, Scikit-learn, Pandas, NumPy, Pickle  
- **Dataset**: IMDb Top 1000 movies (`imdb_top_1000.csv`)

---

## 🚀 How It Works
1. Preprocess the IMDb dataset and create a **movie dictionary** (vectorized features).  
2. Store processed data in `movie_recommendation.pkl`.  
3. Use **cosine similarity** to find the most similar movies to the one chosen.  
4. Display results in a **modern UI** with movie posters, release year, genre, and director.

---

## 📂 Project Structure
├── app.py # Streamlit app with styled UI
├── recom_functions.py # Functions for recommendations and poster links
├── process.ipynb # Preprocessing & feature extraction notebook
├── imdb_top_1000.csv # Dataset used
├── movie_recommendation.pkl # Preprocessed movie dictionary + dataframe
├── premium_photo.jpg # Background image for UI
└── README.md # Project documentation



🎯 Example Output
If you select "The Dark Knight", recommendations might be:

Batman Begins

Inception

The Prestige

Interstellar

Man of Steel

Each recommendation shows:

🎬 Poster

📅 Release Year

👨‍🎤 Director

🏷️ Genres (as styled chips)

