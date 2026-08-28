import streamlit as st

st.title("Programming Languages")
st.header("Languages that let you build.")

lang = st.selectbox("Languages: ",["Python","JavaScript","Linux","SQL","R","HTML","CSS","Java"])

st.write(f"You have selected **{lang}**")
st.text("Congratulations!")
st.success("You have successfully selected a language.")