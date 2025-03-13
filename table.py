import streamlit as st
import pandas as pd


# Sample data
data = {
    "Product": ["Laptop", "Smartphone", "Headphones", "Tablet"],
    "Competitor A": [1200, 800, 150, 600],
    "Competitor B": [1250, 820, 140, 620],
    "Competitor C": [1190, 790, 160, 590],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title("Competitor Price Comparison Table")

# Display the table
st.write("### Product Prices")
st.dataframe(df)

# Add sorting functionality
st.sidebar.header("Sort Options")
sort_by = st.sidebar.selectbox("Sort by", ["Product", "Competitor A", "Competitor B", "Competitor C"])
ascending = st.sidebar.checkbox("Ascending", True)
df_sorted = df.sort_values(by=sort_by, ascending=ascending)
st.write("### Sorted Table")
st.dataframe(df_sorted)

# Add search functionality
st.sidebar.header("Search")
search_term = st.sidebar.text_input("Search by Product Name")
if search_term:
    df_filtered = df[df["Product"].str.contains(search_term, case=False)]
    st.write("### Filtered Table")
    st.dataframe(df_filtered)