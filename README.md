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

