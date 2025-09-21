import streamlit as st

st.title("CORD-19 COVID-19 Research Explorer")
st.write("Explore research publications from the CORD-19 dataset")

# Show sample data
st.subheader("Sample Data")
st.dataframe(df_clean.head())

# Interactive: select year
year = st.slider("Select Year", int(df_clean['year'].min()), int(df_clean['year'].max()))
st.write("Papers in selected year:", (df_clean['year'] == year).sum())

# Publications over time chart
st.subheader("Publications Over Time")
st.line_chart(papers_per_year)

# Top journals
st.subheader("Top Journals")
st.bar_chart(top_journals)

