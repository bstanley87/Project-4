import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv(r"C:\Users\breea\OneDrive\Documents\GitHub\Project-4\vehicles_us.csv")

st.title("Car Advertisement Dashboard")
st.header("Exploratory Data Analysis")

st.subheader("Price Distribution")
fig_price = px.histogram(df, x='price', nbins=50, title="Price Distribution")
st.plotly_chart(fig_price)

st.subheader("Scatter Plot: Odometer vs. Price")
fig_scatter = px.scatter(df, x='odometer', y='price', color='condition', title="Odometer vs. Price")
st.plotly_chart(fig_scatter)


st.subheader("Filter High-Value Cars")
high_value = st.checkbox("Show cars priced above $50,000")
if high_value:
    filtered_df = df[df['price'] > 50000]
    st.write(f"Showing {len(filtered_df)} cars priced above $50,000")
  
    fig_filtered = px.scatter(filtered_df, x='odometer', y='price', color='condition', title="High-Value Cars: Odometer vs. Price")
    st.plotly_chart(fig_filtered)

  


