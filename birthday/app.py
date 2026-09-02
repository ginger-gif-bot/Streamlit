import streamlit as st
import os
import time

style = os.path.join("birthday","style.css")
with open(style) as f:
     st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = 1

if "page3_frame" not in st.session_state:
        st.session_state.page3_frame = 0

page_cont = st.empty()

if st.session_state.page == 1:
    with page_cont.container():
        st.title("Guess What ?👀")
        col1,col2,col3 = st.columns([0.8,1,1])
        with col2:
            st.markdown("<br><br>",unsafe_allow_html=True)
            if st.button("What ?🤔"):
                st.session_state.page +=1
                st.rerun()

elif st.session_state.page == 2:
    with page_cont.container():
        st.markdown(f"""
                <div class="birthday-title">
                <h1 style='margin-top: 0px; color: #e6ceaf;'>
                Someone's Birthday is Today...😏🫢🎂
                </h1>
                </div>
    """,unsafe_allow_html=True)
        st.markdown(
            f"""<div class="scroll">(Scroll down ↓↓↓↓↓😗)</div>""",
                unsafe_allow_html=True)
        col1,col2,col3 = st.columns([0.8,1,1])
        with col2:
            st.markdown("<br><br>",unsafe_allow_html=True)
            if st.button("Whose ?😁"):
                st.session_state.page +=1
                st.rerun()
        
elif st.session_state.page == 3:
    frames = [
        """<h1> Hmm... </h1>""",
        """<h1> Let's See... </h1>""",
        """<h1> Who could it be? 🤔 </h1>""",
        """<h1> Ohh!!!🫢 </h1>""",
        """<div class='page3'><h1> It's my🎀 FAVORITE❤️ person's Birthday </h1></div>""",
    ]
    
    if st.session_state.page3_frame < len(frames):
        page_cont.markdown(frames[st.session_state.page3_frame], unsafe_allow_html=True)
        time.sleep(1)
        st.session_state.page3_frame += 1
        st.rerun()
    else:
        with page_cont.container():
            col1,col2,col3 = st.columns([1,2,1])
            with col2:
                st.markdown("<br><br>",unsafe_allow_html=True)
                st.button("But who is it? ❤️")
                st.markdown("<h4>Enter your name:</h4>",unsafe_allow_html=True)
                name = st.text_input(" ",label_visibility="hidden").upper()
                if name == "SNEHAL":
                    st.session_state.page +=1
                    st.rerun()
                elif name != "":
                    st.markdown("<h3>It's not you!!🙃</h3>",unsafe_allow_html=True)

elif st.session_state.page == 4:
    st.write("avaxvasuv")