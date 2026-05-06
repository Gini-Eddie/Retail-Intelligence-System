# Price Recommendation System 💰

A machine learning project that analyzes retail sales data and builds a price recommendation system based on demand patterns, market segmentation, and regional variations.

## 📋 Project Overview

This project processes retail sales transaction data (~4.5 million records) across multiple African countries and cities to:
- Engineer realistic demand patterns based on geographic tiers
- Correlate pricing with demand variations
- Create actionable insights for price optimization
- Build a predictive model for price recommendations

## 🌍 Data Scope

- **Countries**: Nigeria, Kenya, South Africa, Ghana, Egypt
- **Geographic Segmentation**: Tier 1 (Major cities) vs Tier 2 (Mid-level cities)
- **Products**: 50+ items across Electronics, Fashion, and Home categories
- **Timespan**: Multiple years of transaction history
- **Records**: ~4.5 million retail transactions

## 📊 Key Features Engineered

### Demand Engineering
- **Tier 1 (Major cities)**: 2.5x higher demand than Tier 2
- Realistic market behavior reflecting urban vs mid-level dynamics
- Seeded randomization for reproducibility

### Price Engineering
- **Base Prices**: Product category-specific pricing ranges
- **Demand Correlation**: Weak positive correlation (r ≈ 0.21) for realism
- **Noise Addition**: ±10% variation to simulate real market conditions
- **Strategy**: Premium pricing for high-demand items, competitive pricing for low-demand

### Store Network
- Multiple stores per location (Tier 1 ≈ 50-55 stores, Tier 2 ≈ 45-55 stores)
- Country-based store organization
- Unique store IDs for each location

## 🗂️ Project Structure

```
portfolio-1-start/
├── data/
│   ├── raw/
│   │   └── retail_sales.csv          # Original transaction data
│   └── processed/
│       └── cleaned_retail_sales.csv  # Engineered & enriched dataset
├── notebooks/
│   ├── data_exploration_and_cleaning.ipynb   # Main ETL pipeline
│   └── eda-explore.ipynb                      # Exploratory data analysis
├── api/                               # FastAPI endpoints (future)
├─��� src/                               # Production code modules (future)
├── main.py                            # Entry point (future)
├── requirements.txt                   # Python dependencies
├── README.md                          # This file
└── .gitignore                         # Git ignore rules
```

## 📈 Key Metrics

| Metric | Value |
|--------|-------|
| Total Records | ~4.5 Million |
| Unique Stores | 500+ |
| Unique Products | 50+ |
| Countries | 5 |
| Price-Demand Correlation | 0.21 (weak positive) |
| Tier 1/Tier 2 Demand Ratio | 2.5x |

## 🚀 Quick Start

### 1. Clone & Setup
```bash
git clone https://github.com/yourusername/Price-Recommendation.git
cd Price-Recommendation
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
# or
source venv/bin/activate      # On macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Data Processing
```bash
jupyter notebook notebooks/data_exploration_and_cleaning.ipynb
```

This will:
- Load raw retail sales data
- Engineer demand patterns by geographic tier
- Create price-demand correlations
- Generate the cleaned dataset: `data/processed/cleaned_retail_sales.csv`

### 5. Explore Results
```bash
jupyter notebook notebooks/eda-explore.ipynb
```

View visualizations including:
- Price vs Demand correlation scatter plots
- Demand distribution by city tier
- Product category analysis
- Geographic insights

## 🔧 Technology Stack

- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **ML/Statistics**: Scikit-learn, SciPy
- **Notebooks**: Jupyter, JupyterLab
- **API Framework**: FastAPI, Uvicorn
- **Data Validation**: Pydantic

## 📝 Data Processing Pipeline

### Phase 1: Data Enrichment
- Load raw transaction data
- Map stores to countries and city tiers
- Create location-based store network
- Assign products to categories/subcategories

### Phase 2: Feature Engineering
- Tier-based demand adjustment (2.5x for Tier 1)
- Base price generation by product category
- Temporal features (year, month, day_of_week, is_weekend)

### Phase 3: Price-Demand Correlation
- Normalize demand to 0-1 scale
- Calculate demand-based price factor (0.8-1.5x multiplier)
- Add realistic noise (±10%) for variation
- Generate final prices with weak positive correlation

## 📊 Correlation Analysis

The **Price-Demand correlation of 0.21** indicates:
- Weak positive relationship (as demand ↑, price tends to ↑)
- Realistic market behavior (not perfectly correlated)
- Influence of other factors: seasonality, competition, inventory, promotions

## 🔍 Data Quality Features

- ✅ Seeded randomization for reproducibility
- ✅ Realistic demand distributions by geography
- ✅ Vectorized operations for 100x faster processing
- ✅ No data leakage between stores and countries
- ✅ Consistent price-demand relationships

## 🎯 Next Steps

- [ ] Build predictive model for price optimization
- [ ] Implement FastAPI REST endpoints
- [ ] Deploy to production
- [ ] Add real-time data ingestion
- [ ] Create dashboard for insights
- [ ] A/B testing framework for pricing strategies

## 📚 Notebooks Guide

### `data_exploration_and_cleaning.ipynb`
The main ETL pipeline. Contains:
- Raw data loading and exploration
- Store network engineering
- Product hierarchy creation
- Demand tier-based adjustments
- Price-demand correlation engineering
- Output: `cleaned_retail_sales.csv`

**Performance**: ~30-60 seconds (fully vectorized)

### `eda-explore.ipynb`
Exploratory analysis and visualization. Contains:
- Statistical summaries
- Distribution analysis
- Price vs demand correlation charts
- Geographic insights
- Category-level analysis

## ⚠️ Important Notes

- All data is **synthetically engineered** for demonstration purposes
- Random seeds ensure **reproducibility** across runs
- Vectorized NumPy operations for **efficient processing**
- Dataset reflects realistic market dynamics

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

Created as a portfolio project for data science and machine learning practice.

## 🤝 Contributing

Feel free to fork, modify, and submit pull requests!

---

**Last Updated**: May 2026
