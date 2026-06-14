import os
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'
OUTPUTS_DIR = BASE_DIR / 'outputs'

# =====================================================================
# SYSTEM INITIALIZATION & STYLING SETUP
# =====================================================================
def initialize_environment():
    """Ensures directories exist and sets corporate visualization themes."""
    OUTPUTS_DIR.mkdir(exist_ok=True)
    
    # Establish a clean, professional theme for static graphics
    sns.set_theme(style="whitegrid")
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 11
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    print("🚀 Environment initialized and visual themes established.")

# =====================================================================
# PHASE 2: ROBUST DATA ENGINEERING PIPELINE
# =====================================================================
def run_data_pipeline(input_path, output_path):
    """Loads, cleans, transforms, and exports the Netflix dataset."""
    print(f"⏳ Loading raw dataset from: {input_path}")
    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"CRITICAL ERROR: Source file not found at {input_path}. Place 'netflix_titles.csv' in your 'data/' folder.")

    print("🧹 Cleaning missing value vectors...")
    # Impute massive missing categorical variables to preserve rows for calculations
    df['country'] = df['country'].fillna('Unknown')
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')

    # Drop rows with minimal missing values where engineering relies on accuracy
    df.dropna(subset=['date_added', 'rating'], inplace=True)

    print("📅 Engineering advanced temporal features...")
    # Standardize and clean text-based dates into ISO Datetime objects
    df['date_added'] = df['date_added'].str.strip()
    df['date_added'] = pd.to_datetime(df['date_added'], format='%B %d, %Y', errors='coerce')
    df.dropna(subset=['date_added'], inplace=True) # Clear any formatting anomalies

    # Extract granular features for executive reporting
    df['year_added'] = df['date_added'].dt.year.astype(int)
    df['month_added'] = df['date_added'].dt.month_name()

    print("⏱️ Parsing and normalizing runtime scales...")
    # Extract numerical scalar from strings like "90 min" or "2 Seasons"
    df['duration_numeric'] = df['duration'].apply(lambda x: int(str(x).split()[0]) if pd.notnull(x) else 0)

    # Save clean state for Power BI downstream deployment
    df.to_csv(output_path, index=False)
    print(f"✅ Clean pipeline executed. Data saved to: {output_path}")
    return df

# =====================================================================
# PHASE 3: METRIC ANALYSIS & PRESENTATION GRAPHICS
# =====================================================================
def generate_business_graphics(df):
    """Generates and exports presentation-ready visual metrics."""
    print("⏳ Creating core executive visuals...")

    # --- Chart 1: Catalog Strategic Inventory Split (Pie/Donut) ---
    type_counts = df['type'].value_counts()
    fig_donut = px.pie(
        names=type_counts.index, 
        values=type_counts.values, 
        hole=0.4,
        title="Netflix Catalog Distribution Strategy: Movies vs TV Shows",
        color_discrete_sequence=['#E50914', '#221F1F'] # Premium Netflix Brand Identity
    )
    fig_donut.update_traces(textinfo='percent+label')
    fig_donut.write_image(OUTPUTS_DIR / 'content_type.png')

    # --- Chart 2: Content Scaling Trajectory Curve (Line Graph) ---
    # Filter for standard scaling era to ensure a meaningful trend line
    trend_df = df.groupby(['year_added', 'type']).size().reset_index(name='count')
    trend_df = trend_df[(trend_df['year_added'] >= 2010) & (trend_df['year_added'] <= 2021)]

    plt.figure()
    sns.lineplot(
        data=trend_df, x='year_added', y='count', hue='type', 
        marker='o', palette=['#E50914', '#221F1F'], linewidth=2.5
    )
    plt.title('Velocity of Content Additions to Netflix Catalog (2010 - 2021)', fontweight='bold')
    plt.xlabel('Year Content Was Added')
    plt.ylabel('Volume of Titles Uploaded')
    plt.tight_layout()
    plt.savefig(OUTPUTS_DIR / 'yearly_growth.png', dpi=300)
    plt.close()

    # --- Chart 3: Unnesting Categorical Vectors (Genre Tracking) ---
    # Explode comma-separated strings ("Dramas, Independent Movies") into individual distinct rows
    genres_df = df.assign(listed_in=df['listed_in'].str.split(', ')).explode('listed_in')
    top_genres = genres_df['listed_in'].value_counts().head(12)

    plt.figure()
    sns.barplot(x=top_genres.values, y=top_genres.index, palette='Reds_r')
    plt.title('Top 12 Prevalent Content Genres Across Platform Catalog', fontweight='bold')
    plt.xlabel('Total Catalog Asset Count')
    plt.ylabel('Genre Categorization')
    plt.tight_layout()
    plt.savefig(OUTPUTS_DIR / 'top_genres.png', dpi=300)
    plt.close()

    # --- Chart 4: Optimization Analysis of Feature Film Length (Histogram) ---
    movies_only = df[df['type'] == 'Movie']

    plt.figure()
    sns.histplot(data=movies_only, x='duration_numeric', bins=40, kde=True, color='#E50914')
    plt.axvline(movies_only['duration_numeric'].mean(), color='#221F1F', linestyle='--', 
                label=f"Catalog Runtime Average: {movies_only['duration_numeric'].mean():.1f} mins")
    plt.title('Statistical Distribution Pattern of Movie Runtimes', fontweight='bold')
    plt.xlabel('Duration in Minutes')
    plt.ylabel('Frequency Distribution Count')
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUTS_DIR / 'duration_distribution.png', dpi=300)
    plt.close()

    print("✅ Executive visualizations successfully exported to 'outputs/' directory.")

# =====================================================================
# EXECUTION CONTROLLER
# =====================================================================
if __name__ == "__main__":
    RAW_DATA_PATH = DATA_DIR / 'netflix_titles.csv'
    CLEAN_DATA_PATH = DATA_DIR / 'netflix_cleaned.csv'
    
    # Run pipeline stages sequentially
    initialize_environment()
    cleaned_dataframe = run_data_pipeline(RAW_DATA_PATH, CLEAN_DATA_PATH)
    generate_business_graphics(cleaned_dataframe)
    print("🎉 Entire portfolio pipeline has executed flawlessly!")

    # Add all new code, data schemas, and visualization graphics
git add notebooks/ outputs/ data/netflix_cleaned.csv

# Commit with professional engineering notation
git commit -m "Completed core analytics engine: functionalized data cleaner and generated executive visuals"