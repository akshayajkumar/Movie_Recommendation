# 🎬 Movie Recommendation System

This project is a Machine Learning-powered web application that recommends movies similar to the one selected by the user.  
It uses **content-based filtering** with **cosine similarity** on preprocessed movie feature vectors. The app is built with **Streamlit** and styled with a modern UI.

---

## 📌 Features

- 🎥 Recommends top **N similar movies** based on your selection  
- 🖼️ Displays **poster, release year, director, and genres**  
- 🧠 Powered by a pre-trained similarity model (`.pkl`)  
- 🖥️ Interactive and styled UI with **Streamlit**  
- 🌄 Uses a background image for immersive experience  

---

## 🚀 Live Demo

👉 Try the app here: [Movie Recommendation System](https://akshayajkumar-movie-recommendation.streamlit.app)

---

## 🗂️ Project Files

| File | Description |
|------|-------------|
| `app.py` | Streamlit application code with custom styling |
| `recom_functions.py` | Functions for recommendation (cosine similarity + poster handling) |
| `process.ipynb` | Notebook for preprocessing and feature extraction |
| `imdb_top_1000.csv` | Dataset of IMDb Top 1000 movies |
| `movie_recommendation.pkl` | Pickled movie dictionary + dataframe for fast retrieval |
| `premium_photo.jpg` | Background image for the app |
| `README.md` | Project documentation |

---

## 🎯 Example Output

If you select **"The Dark Knight"**, recommendations might be:

- Batman Begins  
- Inception  
- The Prestige  
- Interstellar  
- Man of Steel  

Each recommendation includes:
- 🎬 Poster  
- 📅 Release Year  
- 👨‍🎤 Director  
- 🏷️ Genres (as styled chips)  

---

## 🧰 Tech Stack

- **Frontend/UI**: Streamlit  
- **Backend/Model**: Scikit-learn (cosine similarity)  
- **Language**: Python  
- **Dataset**: IMDb Top 1000  
- **Other Tools**: pandas, numpy, pickle  

---
## 🎯 Example Output

If you select **"The Dark Knight"**, recommendations might be:

- Batman Begins  
- Inception  
- The Prestige  
- Interstellar  
- Man of Steel  

Each recommendation includes:
- 🎬 Poster  
- 📅 Release Year  
- 👨‍🎤 Director  
- 🏷️ Genres (as styled chips)  

---


