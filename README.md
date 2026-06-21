Markdown
# 🎬 Entertainment Intelligence: End-to-End Analytics Engine & ML Recommender

## 📌 Strategic Overview
This repository delivers an enterprise-grade data science framework that inspects, visualizes, and models Netflix's global streaming catalog. Moving from descriptive analytics to predictive modeling, the project functions across two distinct operational pillars: a corporate business intelligence pipeline tracking content strategy variations, and a deployed machine learning engine predicting user consumption behaviors.

### 🎯 Core Objectives Realized
* **Catalog Mix Analysis:** Automated data extraction evaluating the exact operational allocation splits between episodic TV series and feature films.
* **Parametric Optimization:** Statistical modeling of asset lengths to identify the exact runtime thresholds optimized for home audience retention.
* **Predictive Asset Mapping:** Architecting a content-based filtering system to calculate spatial similarity vectors across complex text metadata records.
* **Application Deployment:** Packaging the underlying machine learning models into an interactive, cloud-ready web interface for end-user interaction.

---

## 🛠 Project Workspace Architecture
```text
├── data/
│   ├── netflix_titles.csv         # Raw metadata source file
│   └── netflix_cleaned.csv        # Post-pipeline standardized dataset
├── notebooks/
│   ├── netflix_analysis.py        # Automated cleaning & visualization script
│   ├── netflix_recommender.py     # Mathematical machine learning backend engine
│   └── app.py                     # Interactive Streamlit UI web application layer
├── outputs/
│   ├── content_type.png           # Visualizing platform inventory mix
│   ├── yearly_growth.png          # Visualizing historical scaling trajectories
│   ├── top_genres.png             # Pareto tracking of catalog genre dominance
│   └── duration_distribution.png  # Parametric distribution modeling of asset lengths
├── dashboards/
│   └── netflix_dashboard.pbix     # Dark-theme Power BI executive workspace file
└── requirements.txt               # System dependencies configuration
⚙️ Data Engineering & Pipeline Transformations
Raw streaming metadata is unstructured and inconsistent. This pipeline implements a functionalized Python preprocessing engine:

Strategic Imputation: Identified systemic missing vectors in categorical attributes (director, cast, country) and converted them to an explicit "Unknown" state to preserve records for downstream multi-categorical metrics.

Granular Feature Splitting: Extracted clean year_added and month_added indicators from chaotic text string timestamps to perform temporal growth analysis.

Metric Standardization: Isolated and stripped text units (such as 'min') from raw runtimes, casting records into pure mathematical integers (duration_numeric) to enable parametric distribution modeling.

🧠 Machine Learning Engine & System Design
To move from tracking what happened to predicting consumer preference, the engine implements a text-based semantic matching framework:

Metadata Feature Fusion: Combined structural metadata components (description, listed_in, cast, director) into a unified text document corpus per asset.

TF-IDF Vectorization: Initialized text vectorization filtering out standard English stop words, translating text features into numerical vectors where unique, high-value industry definitions are weighted appropriately.

Cosine Similarity Calculations: Computed the dot product values across all spatial vectors to measure the angle between content assets. Titles returning scores nearest to 1.0 are isolated as high-probability recommendations.

📊 Strategic Business Revelations
1. The Churn Reduction Pivot
While feature films make up 69.6% of Netflix’s historical catalog compared to TV shows at 30.4%, trend tracking indicates a pronounced growth stabilization in movies post-2019. Netflix is prioritizing long-form, episodic serial commitments which dramatically improve monthly user retention and reduce subscriber churn.

2. The 95-Minute Engineering Threshold
Parametric mapping of film runtimes yields a clean normal distribution centered precisely between 95 and 100 minutes. This validates an intentional operational sweet spot engineered around home streaming attention cycles to maximize title completion metrics.

🚀 Environment Deployment & Quickstart
1. Clone & Initialize Local Environment
Bash
git clone [https://github.com/indra-swe/netflix-data-analysis.git](https://github.com/indra-swe/netflix-data-analysis.git)
cd netflix-data-analysis
pip install -r requirements.txt
2. Execute the Analytical Script Pipeline
To re-run the engineering pipeline and overwrite the static visual files inside outputs/:

Bash
python notebooks/netflix_analysis.py
3. Launch the Interactive Web Application
To boot up the local machine learning web server and navigate the recommendation engine using a graphical user interface:

Bash
streamlit run notebooks/app.py