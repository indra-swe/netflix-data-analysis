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

# =====================================================================
# CORE DATA CORE LAUNCH
# =====================================================================
@st.cache_data # Caches data in memory so the app stays lightning-fast
def load_and_vectorize_data():
    try:
        df = pd.read_csv('../data/netflix_cleaned.csv')
    except FileNotFoundError:
        df = pd.read_csv('data/netflix_cleaned.csv')
        
    df['description'] = df['description'].fillna('')
    df['listed_in'] = df['listed_in'].fillna('')
    df['cast'] = df['cast'].fillna('')
    df['director'] = df['director'].fillna('')
    
    # Generate identical text profile matching the backend engine
    df['metadata_soup'] = (df['description'] + " " + df['listed_in'] + " " + df['cast'] + " " + df['director']).str.lower()
    
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['metadata_soup'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()
    return df, cosine_sim, indices

# Load cache components safely
df, cosine_sim, indices = load_and_vectorize_data()

