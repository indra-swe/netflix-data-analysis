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
