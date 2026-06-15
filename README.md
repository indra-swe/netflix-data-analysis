# 🎬 Entertainment Intelligence: Engineering & Mapping Netflix's Global Strategy

## 📌 Strategic Overview
This project delivers an end-to-end analytics and data pipeline inspecting Netflix's global content catalog. By parsing, processing, and restructuring unstructured streaming metadata across thousands of assets, this repository reveals how Netflix strategically shifts its programming based on content type, runtime optimization, and international market expansion.

### 🎯 Key Strategic Questions Answered
1. **Catalog Mix Optimization:** How does Netflix balance feature films against episodic TV series to maximize user retention?
2. **Temporal Delivery Velocities:** What do the distribution patterns look like for content additions over the years, and what historical strategy do they reveal?
3. **Runtime Distribution Engineering:** What is the structural sweet spot for content duration designed for modern home streaming?

---

## 🛠 Structural Mapping & Components
```text
├── data/
│   ├── netflix_titles.csv         # Raw metadata source file
│   └── netflix_cleaned.csv        # Post-pipeline standardized dataset
├── notebooks/
│   └── netflix_analysis.py        # Complete automated transformation & visualization script
├── outputs/
│   ├── content_type.png           # Visualizing platform inventory mix
│   ├── yearly_growth.png          # Visualizing historical scaling trajectories
│   ├── top_genres.png             # Pareto tracking of catalog genre dominance
│   └── duration_distribution.png  # Parametric distribution modeling of asset lengths
├── dashboards/
│   └── netflix_dashboard.pbix     # Dark-theme Power BI executive workspace file
└── requirements.txt               # Declared system dependencies

⚙️ Data Engineering & Pipeline Transformations
Raw metadata is notoriously messy and unfit for production analytics. This project implements a Python-based data engineering pipeline to clean and prepare the data:

Strategic Imputation: Identified systemic missing variables in categorical strings (director, cast, country) and converted them to an explicit "Unknown" status to preserve rows for other categorical metrics.

Granular Feature Splitting: Extracted clean year_added and month_added indicators from erratic text string timestamps to perform temporal growth analysis.

Metric Standardization: Isolated and removed text units (such as 'min') from film runtime data, casting the remaining data as pure mathematical integers (duration_numeric) to enable accurate distribution and average modeling.

📊 Core Business Revelations
1. The Retention Paradox (Movies vs. TV Shows)
While feature films make up 69.6% of Netflix’s historical catalog compared to TV shows at 30.4%, trend analysis shows that volume growth for movies has slowed since 2019. Netflix is consciously shifting capital toward multi-season episodic series to keep users engaged and reduce platform churn.

2. The 95-Minute Engineering Threshold
Plotting film runtimes reveals a clear normal distribution centered tightly between 95 and 100 minutes. This confirms an operational sweet spot engineered for home streaming attention spans, keeping viewers engaged and helping maximize completion metrics.

🚀 Step-by-Step Environment Execution
1. Clone & Initialize Dependency Environments
Bash
git clone [https://github.com/indra-swe/netflix-data-analysis.git](https://github.com/indra-swe/netflix-data-analysis.git)
cd netflix-data-analysis
pip install -r requirements.txt
2. Run the Processing Engine
To re-run the entire pipeline, process the data, and update the static graphics inside outputs/, run the main script:

Bash
python notebooks/netflix_analysis.py