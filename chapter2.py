import streamlit as st
import time
st.title("Chai Maker")
st.header("Your personel chai maker")

st.subheader("Select your custom chai:")

name = st.text_input("Enter your name: ")  #text input
if name:
    st.write(f"Welcome {name}, \nWhat would you like to have?")
tea_type = st.selectbox("Chai: ",["Masala chai","Adrak chai","kali chai","doodh wali chai"])
st.write(f"You have selected {tea_type}")

base = st.radio("Select Base:",["Cow milk","Almond milk","Water","Pink milk"])
sweetness = st.radio("Select your sweetness level: ",["Very sweet","Medium sweet","Less sweet","No sugar"])
t = st.slider("In how many minutes you want the tea: ",5,20,12)
# here 5 is the bottom,20 is the highest and 12 is the default
cups = st.number_input("How many cups: ",min_value=1,max_value=10,step=1)
# number input
# step is by how much you want to increase the number
if st.button("Make Chai"):
    if name:
        st.success(f"Hey, {name}...\nYour chai is being brewed.")
    st.write(f"Your {tea_type} is being ready.")
    st.write(f"Your tea with {base} base is being ready.")
    st.write(f"Your sweetness level is {sweetness}.")
    st.write(f"Your {cups} cups are coming right up!!")
    st.write(f"Your tea will be ready in {t} minutes")

dob = st.date_input("Enter your DOB: ")
dt = st.datetime_input("Enter datetime: ")