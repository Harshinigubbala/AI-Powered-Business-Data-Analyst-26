import streamlit as st
import plotly.express as px

from analysis import (
    load_data, get_business_summary, get_product_analysis,
    get_country_analysis, get_monthly_analysis
)
from qa_engine import answer_question

st.set_page_config(page_title="AI-Powered Business Data Analyst", page_icon="📊", layout="wide")
df = load_data()

st.title("📊 AI-Powered Business Data Analyst")
st.caption("Exploration of UCI Online Retail transaction data. Sales are calculated as Quantity × UnitPrice.")

st.sidebar.header("Dashboard Filters")
countries = st.sidebar.multiselect("Country", sorted(df["Country"].dropna().unique()), default=sorted(df["Country"].dropna().unique()))
years = st.sidebar.multiselect("Year", sorted(df["Year"].unique()), default=sorted(df["Year"].unique()))
filtered = df[df["Country"].isin(countries) & df["Year"].isin(years)]

summary = get_business_summary(filtered)
st.header("Business Summary")
cols = st.columns(4)
for col, (label, value) in zip(cols, summary.items()):
    col.metric(label, f"£{value:,.2f}" if "Sales" in label else f"{value:,}")

left, right = st.columns(2)
country_data = get_country_analysis(filtered).head(15)
left.subheader("Sales by Country")
left.plotly_chart(px.bar(country_data, x="Country", y="Total_Sales", title="Top 15 countries by sales"), use_container_width=True)

product_data = get_product_analysis(filtered).head(15)
right.subheader("Top Products")
right.plotly_chart(px.bar(product_data, x="Total_Sales", y="Description", orientation="h", title="Top 15 products by sales"), use_container_width=True)

monthly = get_monthly_analysis(filtered)
st.subheader("Monthly Sales Trend")
st.plotly_chart(px.line(monthly, x="Year-Month", y="Total_Sales", markers=True), use_container_width=True)

st.subheader("Filtered Transaction Data")
st.dataframe(filtered, use_container_width=True)

st.header("Ask Your Business Data")
if "previous_question" not in st.session_state:
    st.session_state.previous_question = None
question = st.text_input("Ask about sales, quantity, invoices, countries, products, or trends.",
                         placeholder="Which country has the highest sales?")
if st.button("Get Answer"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        result = answer_question(filtered, question, st.session_state.previous_question)
        st.subheader("Answer")
        st.success(result["answer"])
        st.subheader("Analysis Steps")
        st.write(result["steps"])
        if result["data"] is not None:
            st.subheader("Supporting Results")
            st.dataframe(result["data"], use_container_width=True)
        if result["data"] is not None:
            st.session_state.previous_question = question

st.caption("Source: UCI Machine Learning Repository, Online Retail dataset. Dataset cleaning and assumptions are documented in readme.md.")
