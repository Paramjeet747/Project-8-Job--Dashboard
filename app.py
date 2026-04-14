import streamlit as st
import pandas as pd
st.title("My Job Dashboard")
df = pd.read_csv("final_clean_data_project8.csv")
st.write(df.head())
st.header("📚Job Category Count")
st.bar_chart(df['category'].value_counts())
st.subheader("Full Job Data")
st.dataframe(df)
df.columns = df.columns.str.strip()
st.subheader("Search Jobs")
search = st.text_input("Search job title")
if search:
    result = df[df['title'].str.contains(search, case=False, na=False)]
    st.dataframe(result)
    

