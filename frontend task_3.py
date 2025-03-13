import streamlit as st
import pandas as pd

data = {
    "Product": ["Smart TV", "Gaming Console", "Wireless Earbuds", "Smartwatch"],
    "Competitor A": [45000, 32000, 3500, 8000],
    "Competitor B": [46000, 31000, 3400, 8200],
    "Competitor C": [44000, 33000, 3600, 7900],
}
df = pd.DataFrame(data)
st.title("Competitor Price Comparison Table")
st.write("### Product Prices")
st.dataframe(df)
st.sidebar.header("Sort Options")
sort_by = st.sidebar.selectbox("Sort by", ["Product", "Competitor A", "Competitor B", "Competitor C"])
ascending = st.sidebar.checkbox("Ascending", True)
df_sorted = df.sort_values(by=sort_by, ascending=ascending)
st.write("### Sorted Table")
st.dataframe(df_sorted)
st.sidebar.header("Search")
search_term = st.sidebar.text_input("Search by Product Name")
if search_term:
    df_filtered = df[df["Product"].str.contains(search_term, case=False)]
    st.write("### Filtered Table")
    st.dataframe(df_filtered)
