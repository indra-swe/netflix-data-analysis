import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# =====================================================================
# 1. DATA LOADING & TEXT AGGREGATION
# =====================================================================
print("⏳ Loading cleaned dataset...")
try:
    df = pd.read_csv('../data/netflix_cleaned.csv')
except FileNotFoundError:
    # Fallback to local directory if paths differ
    df = pd.read_csv('data/netflix_cleaned.csv')

# Drop rows with missing crucial text elements for recommendation safety
df['description'] = df['description'].fillna('')
df['listed_in'] = df['listed_in'].fillna('')
df['cast'] = df['cast'].fillna('')
df['director'] = df['director'].fillna('')

print("⚙️ Creating metadata corpus ('Text Soup')...")
# Combine features into a single unified text profile per asset
df['metadata_soup'] = (
    df['description'] + " " + 
    df['listed_in'] + " " + 
    df['cast'] + " " + 
    df['director']
)

# Clean up casing to ensure matching uniformity
df['metadata_soup'] = df['metadata_soup'].str.lower()


# =====================================================================
# 2. MATHEMATICAL VECTORIZATION & SIMILARITY MATRIX
# =====================================================================
print("🧮 Initializing TF-IDF Vectorizer and eliminating stop words...")
# stop_words='english' removes meaningless structural filler text like 'and', 'the', 'is'
tfidf = TfidfVectorizer(stop_words='english')

# Construct the TF-IDF feature matrix
tfidf_matrix = tfidf.fit_transform(df['metadata_soup'])
print(f"📊 Matrix constructed with shape: {tfidf_matrix.shape}")

print("📐 Computing multi-dimensional Cosine Similarity Matrix...")
# Compute the linear dot product to get the similarity matrix scores
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Create a reverse mapping sequence of titles and dataframe indices 
# This helps us instantly look up a movie's row number by typing its name
indices = pd.Series(df.index, index=df['title'].str.lower()).drop_duplicates()
