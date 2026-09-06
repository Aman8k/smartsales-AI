import os
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="SmartSales AI", page_icon="📊", layout="wide"
)

st.title("SmartSales AI 🚀")


# Aapki CSV File load karne ka function
@st.cache_data
def load_data():
    file_path = (
        "data/sales_data.csv"
        if os.path.exists("data/sales_data.csv")
        else "sales_data.csv"
    )

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df["Date"] = pd.to_datetime(df["Date"])
        df["Profit"] = df["Sales"] - df["Cost"]
        return df
    else:
        st.error(
            f"CSV file nahi mili! Dhyan dein ki aapki CSV file path '{file_path}' par sahi se push hui hai."
        )
        return None


df = load_data()

if df is not None:
    # Sidebar Filters
    st.sidebar.header("Filter Options")
    selected_category = st.sidebar.multiselect(
        "Category Chunein",
        options=df["Category"].unique(),
        default=df["Category"].unique(),
    )
    selected_region = st.sidebar.multiselect(
        "Region Chunein",
        options=df["Region"].unique(),
        default=df["Region"].unique(),
    )

    # Filtered Data
    filtered_df = df[
        (df["Category"].isin(selected_category))
        & (df["Region"].isin(selected_region))
    ]

    # Top KPI Metrics
    st.subheader("📈 Real Data Business Overview")
    col1, col2, col3, col4 = st.columns(4)

    total_sales = filtered_df["Sales"].sum()
    total_profit = filtered_df["Profit"].sum()
    total_qty = filtered_df["Quantity"].sum()
    total_cust = filtered_df["Customer"].nunique()

    col1.metric("Total Sales", f"₹{total_sales:,.0f}")
    col2.metric("Total Profit", f"₹{total_profit:,.0f}")
    col3.metric("Items Sold", f"{total_qty}")
    col4.metric("Unique Customers", f"{total_cust}")

    st.markdown("---")

    # Real Charts
    st.subheader("📊 Sales & Category Analytics")

    c1, c2 = st.columns(2)
    with c1:
        st.write("**Date Wise Sales Trend**")
        daily_sales = filtered_df.groupby("Date")["Sales"].sum()
        st.line_chart(daily_sales)

    with c2:
        st.write("**Category Wise Sales**")
        cat_sales = filtered_df.groupby("Category")["Sales"].sum()
        st.bar_chart(cat_sales)

    c3, c4 = st.columns(2)
    with c3:
        st.write("**Region Wise Sales**")
        region_sales = filtered_df.groupby("Region")["Sales"].sum()
        st.bar_chart(region_sales)

    with c4:
        st.write("**Top Selling Products (Quantity)**")
        prod_qty = filtered_df.groupby("Product")["Quantity"].sum()
        st.bar_chart(prod_qty)

    st.markdown("---")

    # Raw Data View
    with st.expander("📄 View CSV Raw Dataset"):
        st.dataframe(filtered_df, use_container_width=True)