import streamlit as st
import pandas as pd
import plotly.express as px

# ✅ Set page config as the first Streamlit command
st.set_page_config(layout="wide")

# Load Data
def load_data():
    df = pd.read_csv("different_products222.csv")

    # ✅ Standardize column names to lowercase and strip spaces
    df.columns = df.columns.str.lower().str.strip()

    # ✅ Rename columns to match expected names
    column_mapping = {
        'product name': 'product',
        'price': 'price',
        'discount': 'discount',
        'date': 'date',
        'source': 'competitor'
    }
    df.rename(columns=column_mapping, inplace=True)

    return df

df = load_data()

# Streamlit UI
st.title("E-Commerce Competitor Strategy Dashboard")

# ✅ Sidebar for Product Selection
if 'product' not in df.columns:
    st.error("Error: The dataset does not contain a 'product' column.")
else:
    product_list = df['product'].unique()
    selected_product = st.sidebar.selectbox("Choose a product to analyze:", product_list)

    # ✅ Filter Data for Selected Product
    filtered_data = df[df['product'] == selected_product]

    # ✅ Display Competitor Pricing Analysis
    st.subheader(f"Competitor Analysis for {selected_product}")
    st.dataframe(filtered_data[['competitor', 'price', 'discount']])

    # ✅ Price Comparison Chart
    fig_price = px.bar(filtered_data, x='competitor', y='price', title="Price Comparison", text='price')
    st.plotly_chart(fig_price, use_container_width=True)

    # ✅ Sentiment Analysis (if available)
    if 'sentiment' in df.columns:
        st.subheader("Customer Sentiment Analysis")
        sentiment_counts = filtered_data['sentiment'].value_counts().reset_index()
        sentiment_counts.columns = ['sentiment', 'count']
        fig_sentiment = px.bar(sentiment_counts, x='sentiment', y='count', title="Sentiment Analysis")
        st.plotly_chart(fig_sentiment, use_container_width=True)

    # ✅ Strategic Recommendations
    st.subheader("Strategic Recommendations")
    st.write("Based on the competitor pricing and customer sentiment analysis, consider the following strategies:")
    st.markdown("- **Competitive Pricing**: Adjust pricing strategies to remain competitive.")
    st.markdown("- **Promotional Offers**: Introduce discounts or offers if competitors are doing so.")
    st.markdown("- **Customer Engagement**: Address negative sentiment by improving customer service and quality.")
