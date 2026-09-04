import streamlit as st
import os, io
import time
import base64
import random
from PIL import Image

style = os.path.join("birthday","style.css")
with open(style) as f:
     st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = 1

if "page3_frame" not in st.session_state:
        st.session_state.page3_frame = 0

page_cont = st.empty()

@st.cache_data
def load_photos(folder,photo_list):
    imgs_html = ""
    for photo in photo_list:
        path = os.path.join(folder,photo)
        img = Image.open(path)
        img.thumbnail((600,300))
        buffer = io.BytesIO()
        img.save(buffer,format="JPEG",quality=75)
        data = base64.b64encode(buffer.getvalue()).decode()
        imgs_html += f"<img src='data:image/jpeg;base64,{data}'>" 
    return imgs_html

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
        """<div class='page3'><h1> Hmm... </h1></div>""",
        """<div class='page3'><h1> Let's See... </h1></div>""",
        """<div class='page3'><h1> Who could it be? 🤔 </h1></div>""",
        """<div class='page3'><h1> Ohh!!!🫢 </h1></div>""",
        """<div class='page3_sp'><h1> It's my🎀 FAVORITE❤️ person's Birthday </h1></div>""",
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
                st.markdown("<h4>Enter your name :</h4>",unsafe_allow_html=True)
                name = st.text_input(" ",label_visibility="hidden").upper()
                if name == "SNEHAL":
                    st.session_state.page +=1
                    st.rerun()
                elif name != "":
                    st.markdown("<h3>It's not you!!🙃</h3>",unsafe_allow_html=True)

elif st.session_state.page == 4:
    with page_cont.container():
        st.markdown(f"""
        <div class='bday'>HAPPY BIRTHDAY</div>
        <div class='name'>Snehal</div>
        """,unsafe_allow_html=True)

        emojis = ["❤️","✨","🎊","🎈","🎉","🎂","🧁","🫶🏻","😘","🌸","🍀"]
        confetti_pieces = ""
        for i in range(30):
            emoji = random.choice(emojis)
            left = random.randint(0, 100)
            delay = round(random.uniform(0, 4), 1)
            duration = round(random.uniform(2, 5), 1)
            size = random.randint(20, 40)
            confetti_pieces += f"<span class='confetti-piece' style='left:{left}%; animation-duration:{duration}s; animation-delay:{delay}s; font-size:{size}px;'>{emoji}</span>"

        st.markdown(f"<div class='confetti-container'>{confetti_pieces}</div>",
                    unsafe_allow_html=True)
        time.sleep(5)
        st.session_state.page += 1
        st.rerun()

elif st.session_state.page == 5:
    folder = r"birthday\photos"
    files = os.listdir(folder)
    row_1 = files[:13]
    row_2 = files[13:27]
    row_3 = files[27:]

    imgs_html_1 = load_photos(folder,tuple(row_1))
    imgs_html_2 = load_photos(folder,tuple(row_2))
    imgs_html_3 = load_photos(folder,tuple(row_3))

    with page_cont.container():
        st.markdown(f"""
            <div class='row-wrapper'>
                <div class='row-left'> {imgs_html_1}</div>
            </div>""",unsafe_allow_html=True)
        st.markdown(f"""
                <div class='row-wrapper'>
                    <div class='row-left'> {imgs_html_2}</div>
                </div>""",unsafe_allow_html=True)
        st.markdown(f"""
                <div class='row-wrapper'>
                    <div class='row-left'> {imgs_html_3}</div>
                </div>""",unsafe_allow_html=True)
        time.sleep(10)
        st.session_state.page +=1
        st.rerun()

elif st.session_state.page == 6:
    col1 ,col2 = st.columns([1,1])
    with col1:
        st.markdown(f"""
            <div class='card'>poem
            </div>
        """,unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div class='card'>msg
            </div>
        """,unsafe_allow_html=True)

    if st.button("One Last Surprise🎁"):
        st.session_state.page +=1
        st.rerun()

elif st.session_state.page == 7:
    with page_cont.container():
        st.video(os.path.join("birthday","video.mov"))
