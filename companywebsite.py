import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")
st.write("""
The day had begun on a bright note. The sun finally peeked through the rain for the first time in a week, 
and the birds were sinf=ging in its warmth. There was no way to anticipate what was about 
to happen. It was a worst-case scenario and there was no way out of it.
""")

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("datacompanytask1.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("imagescompanytask/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("imagescompanytask/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("imagescompanytask/" + row["image"])
