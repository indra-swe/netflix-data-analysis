import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set page layout configuration
st.set_page_config(page_title="Netflix Intelligence Engine", page_icon="🎬", layout="centered")

# Custom styling to match Netflix's premium dark identity
st.markdown("""
    <style>
    .main { background-color: #141414; color: #FFFFFF; }
    h1 { color: #E50914; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    .stSelectbox label { color: #FFFFFF !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 Netflix Content Recommendation Engine")
st.write("Select a movie or TV show below, and our machine learning algorithm will predict your next binge-watch based on systemic metadata analysis.")
