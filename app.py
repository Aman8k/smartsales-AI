import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="SmartSales AI",
    page_icon="📊",
    layout="wide"
)

# Title & Subtitle
st.title("SmartSales AI 🚀")
st.write("Welcome to SmartSales AI Dashboard")

# Sidebar Controls
st.sidebar.header("Filter Options")
time_horizon = st.sidebar.selectbox("Select Time Horizon", ["Last 7 Days", "Last 30 Days", "Year to Date"])

# Sample Data Generation
np.random.seed(42)
dates = pd.date_range(start="2026-08-01", periods=30, freq="D")
sales_data = pd.DataFrame({
    "Date": dates,
    "Sales": np.random.randint(2000, 8000, size=30),
    "Category": np.random.choice(["Electronics", "Fashion", "Home & Kitchen", "Books"], size=30)
})

# KPI Metrics
st.subheader("📈 Performance Overview")
col1, col2, col3, col4 = st.columns(4)

total_revenue = sales_data["Sales"].sum()
avg_order = sales_data["Sales"].mean()
total_orders = len(sales_data)

col1.metric("Total Revenue", f"₹{total_revenue:,.0f}", "+14%")
col2.metric("Total Orders", f"{total_orders}", "+8%")
col3.metric("Avg Order Value", f"₹{avg_order:,.0f}", "+3.2%")
col4.metric("AI Health Index", "96%", "+2%")

st.markdown("---")

# Analytics & Charts Section
st.subheader("📊 Sales Analytics")

col_left, col_right = st.columns([2, 1])

with col_left:
    st.write("**Daily Sales Trend**")
    line_data = sales_data.set_index("Date")[["Sales"]]
    st.line_chart(line_data)

with col_right:
    st.write("**Sales by Category**")
    category_data = sales_data.groupby("Category")["Sales"].sum()
    st.bar_chart(category_data)

st.markdown("---")

# Interactive Button & AI Insights
st.subheader("🤖 AI Analytics Engine")

if st.button("Run Sales Analytics & Generate Report"):
    with st.spinner("Analyzing transaction patterns..."):
        st.success("Analysis Completed!")
        st.markdown("""
        * **Top Performing Category:** Electronics led total sales this period.
        * **Peak Sales Window:** Maximum orders were placed during weekends.
        * **AI Recommendation:** Increase stock for high-demand items to prevent stockouts.
        """)

# Data Table View
with st.expander("View Raw Sales Dataset"):
    st.dataframe(sales_data, use_container_width=True)