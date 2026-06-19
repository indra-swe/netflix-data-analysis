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
