import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Retail AI: Price Optimizer", page_icon="📈", layout="wide")
sns.set_theme(style="whitegrid")



# --- 2. CACHING DATA & MODEL ---
# 1. Load the Data (Cached so it only runs once)
@st.cache_data
def load_data():
    return pd.read_parquet('data/processed/cleaned_retail_sales.parquet')

# 2. Load the Compressed Model (Cached as a resource so it doesn't eat RAM)
@st.cache_resource
def load_model():
    return joblib.load('models/demand_prediction_model_compressed.pkl')

try:
    rf_model = load_model()
    df = load_data()
except Exception as e:
    st.error(f"Error loading files. Make sure your paths are correct: {e}")
    st.stop()


# --- 3. THE OPTIMIZATION ENGINE ---
def run_simulation(product_profile, model, min_price, max_price, step_size=1.0):
    test_prices = np.arange(min_price, max_price + step_size, step_size)
    simulation_df = pd.DataFrame([product_profile] * len(test_prices))
    simulation_df['price'] = test_prices

    simulation_df['predicted_demand'] = model.predict(simulation_df)
    simulation_df['expected_revenue'] = simulation_df['price'] * simulation_df['predicted_demand']

    best_scenario = simulation_df.loc[simulation_df['expected_revenue'].idxmax()]

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x='price', y='expected_revenue', data=simulation_df, color='#2ecc71', linewidth=2.5, ax=ax)

    # Mark the optimal point
    ax.axvline(x=best_scenario['price'], color='#e74c3c', linestyle='--', alpha=0.7)
    ax.plot(best_scenario['price'], best_scenario['expected_revenue'], marker='o', markersize=10, color='#e74c3c')

    ax.set_title('Revenue Simulation Curve', fontsize=14, pad=15)
    ax.set_xlabel('Tested Price ($)', fontsize=12)
    ax.set_ylabel('Expected Revenue ($)', fontsize=12)

    return best_scenario, fig


# --- 4. WEB APP UI (SIDEBAR) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3121/3121693.png", width=60)  # Placeholder logo
st.sidebar.title("Configuration")
st.sidebar.markdown("Configure the product details below to simulate the optimal price.")

# We dynamically extract the unique categories directly from your dataset!
selected_category = st.sidebar.selectbox("Category", df['category'].unique())

# Filter subcategories based on the chosen category so the user can't pick invalid combos
filtered_subcats = df[df['category'] == selected_category]['subcategory'].unique()
selected_subcategory = st.sidebar.selectbox("Subcategory", filtered_subcats)

selected_country = st.sidebar.selectbox("Country", df['country'].unique())
selected_city_tier = st.sidebar.selectbox("City Tier", df['city_tier'].unique())

st.sidebar.markdown("---")
st.sidebar.subheader("Contextual Adjustments")
col1, col2 = st.sidebar.columns(2)
selected_month = col1.slider("Month", 1, 12, 11)
selected_day = col2.slider("Day of Week", 0, 6, 5, help="0=Monday, 6=Sunday")
is_weekend = st.sidebar.checkbox("Is Weekend?", value=True)
selected_store = st.sidebar.number_input("Store ID", min_value=1, max_value=int(df['store_id'].max()), value=15)

# --- 5. WEB APP UI (MAIN DASHBOARD) ---
st.title("📈 AI Price Recommendation Engine")
st.info("**Data Note:** This simulation runs at the *Subcategory* level (e.g., 'Furniture') for demonstration purposes. In a production environment, this engine would be tied directly to individual Product SKUs to account for specific item variations and baseline costs.")
st.markdown(
    "This tool uses a trained Random Forest algorithm to simulate price elasticity and find the exact price point that maximizes total revenue.")

if st.button("🚀 Generate Recommendation", type="primary", use_container_width=True):
    with st.spinner("Running AI Simulation..."):

        # 1. Build the product profile
        product_profile = {
            'store_id': selected_store,
            'category': selected_category,
            'subcategory': selected_subcategory,
            'country': selected_country,
            'city_tier': selected_city_tier,
            'year': 2024,  # Defaulting to current year
            'month': selected_month,
            'day_of_week': selected_day,
            'is_weekend': 1 if is_weekend else 0
        }

        # 2. Reality Check (Historical Bounds)
        historical_data = df[df['subcategory'] == selected_subcategory]
        max_price = historical_data['price'].max()
        min_price = historical_data['price'].min()

        if pd.isna(max_price):
            st.error("Not enough historical data for this combination. Please try another.")
        else:
            # 3. Run Simulation
            best_result, fig = run_simulation(product_profile, rf_model, min_price, max_price)

            # 4. Display Results in beautiful Metric Cards
            st.success("Simulation Complete!")
            st.markdown("### Optimal Pricing Strategy")

            m1, m2, m3 = st.columns(3)
            m1.metric(label="🏆 Recommended Price", value=f"${best_result['price']:,.2f}")
            m2.metric(label="📦 Expected Demand", value=f"{best_result['predicted_demand']:,.0f} units")
            m3.metric(label="💰 Max Projected Revenue", value=f"${best_result['expected_revenue']:,.2f}")

            st.markdown("---")

            # 5. Display the Graph
            st.pyplot(fig)

            # 6. Display Historical Context
            with st.expander("View Historical Data Bounds"):
                st.info(
                    f"The simulation was bounded between **${min_price:.2f}** and **${max_price:.2f}** based on historical sales data for {selected_subcategory}.")
