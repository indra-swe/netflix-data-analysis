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

# =====================================================================
# INTERACTIVE INTERFACE LAYER
# =====================================================================
# Dropdown menu containing sorted alphabetically list of all titles
selected_title = st.selectbox("Search Catalog Asset:", sorted(df['title'].unique()))

if st.button("Generate Recommendations"):
    idx = indices[selected_title]
    
    # If a title has duplicate entries, pick the first index instance safely
    if isinstance(idx, pd.Series):
        idx = idx.iloc[0]
        
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6] # Top 5 selections
    
    movie_indices = [i[0] for i in sim_scores]
    recommendations = df[['title', 'type', 'listed_in', 'description']].iloc[movie_indices]
    
    st.markdown("### 🍿 Top Algorithmic Matches:")
    for i, row in recommendations.iterrows():
        with st.container():
            st.markdown(f"#### 🎥 {row['title']} ({row['type']})")
            st.markdown(f"**🎭 Genres:** *{row['listed_in']}*")
            st.markdown(f"**📝 Synopsis:** {row['description']}")
            st.markdown("---")
