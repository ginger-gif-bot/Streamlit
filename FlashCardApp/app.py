import streamlit as st
import os

if "card" not in st.session_state:
    st.session_state.card = "welcome"

if "count" not in st.session_state:
    st.session_state.count = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

style = os.path.join("FlashCardApp","style.css")
with open(style) as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

st.title("Flash Card")
qtns = [
    {"q" : "What is the Capital of India?","a": "NEW DELHI"},
    {"q": "What does the clock show?","a": "TIME"},
    {"q": "What organ helps us to see?","a":"EYES"}
]

col1, col2, col3 = st.columns([1,6,1])
with col3:
    if st.button("Next"):
        st.session_state.count += 1
        st.session_state.answered = False

with col1:
    if st.button("Previous"):
        st.session_state.count -=1 
        st.session_state.answered = False
    
st.session_state.count = max(0,min(st.session_state.count, len(qtns) -1))
count = st.session_state.count

with col2:
    st.markdown("""<div style='text-align:center'>""",unsafe_allow_html=True)
    st.image(os.path.join("FlashCardApp","img.jpg"),width=60)
    st.markdown("</div>",unsafe_allow_html=True)
    st.markdown(f"""
    <div class='card'> 
    <h2>Question {count+1}</h2>
    <h5> {qtns[count]["q"]} </h5>
    <h4> Your answer </h4>
    </div>
    """,unsafe_allow_html=True)

answer = st.text_input("").upper()
submit = st.button("Submit")

if answer and submit:
    if not st.session_state.answered:
        if answer == qtns[count]["a"]:
            st.success("Congratulations!! You got it correct.")
            st.session_state.score +=1 
            st.session_state.answered = True
        else:
            st.error("Oops! It's wrong.")
        st.markdown(f"<div class='card'> Score: [{st.session_state.score}/3]</div>",unsafe_allow_html=True)

