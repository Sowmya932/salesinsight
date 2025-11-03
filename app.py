import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yaml
from data_loader import load_data
from analysis import compute_kpis, forecast_sales

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

st.set_page_config(
    page_title=config["app"]["title"],
    page_icon=config["app"]["page_icon"]
)

st.title(config["app"]["title"])
st.write(config["app"]["description"])

# File uploader
uploaded_file = st.file_uploader("📤 Upload your sales CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = load_data(config["data"]["sample_file"])

# KPIs
total_sales, avg_order, growth = compute_kpis(df)
col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
col2.metric("🧾 Average Sale", f"${avg_order:,.0f}")
col3.metric("📈 Growth", f"{growth:.2f}%")

# Chart
st.subheader("Monthly Sales Trend")
fig, ax = plt.subplots()
ax.plot(df["Month"], df["Sales"], marker='o', label="Actual Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
plt.xticks(rotation=45)
plt.legend()
st.pyplot(fig)

# Forecast
st.subheader("📅 Sales Forecast")
forecast_df = forecast_sales(df, config["model"]["forecast_periods"])
fig2, ax2 = plt.subplots()
ax2.plot(df["Month"], df["Sales"], marker='o', label="Actual Sales")
ax2.plot(forecast_df["Month"], forecast_df["Sales"], marker='x', linestyle='--', label="Forecast")
plt.xticks(rotation=45)
plt.legend()
st.pyplot(fig2)

# Download option
st.download_button(
    "⬇️ Download Forecast CSV",
    data=forecast_df.to_csv(index=False),
    file_name="forecast.csv",
    mime="text/csv"
)
