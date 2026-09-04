import streamlit as st
import os, io
import time
import base64
import random
from PIL import Image
import time as _time

style = os.path.join("birthday","style.css")
with open(style) as f:
     st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = 1

if "page3_frame" not in st.session_state:
        st.session_state.page3_frame = 0



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

@st.cache_data
def load_audio(path):
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return data

music_map = {
    1: None,
    2: r"birthday\other_music.mp3",
    3: r"birthday\other_music.mp3",
    4: r"birthday\bday_music.mp3",
    5: r"birthday\memory_music.mp3",
    6: r"birthday\letter_music.mp3",
    7: None,
}

current_music = music_map.get(st.session_state.page)
if current_music:
    with open(current_music, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/mp3", autoplay=True, loop=True)
    
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
                    st.markdown("<h3>Nope, not you!!🙃</h3>",unsafe_allow_html=True)

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
    with page_cont.container():
        msg = """
        Dear Snehal,<br><br>

        Once, when the stars fell from the cradle of loneliness,<br>
        I made a wish — to find a friend who could be the twin of me.<br>
        Perhaps the stars listened, because I got you.<br><br>

        I have friends, but no one like you.<br>
        When I speak to you, there's a different kind of comfort — like after a long time,<br>
        I am speaking to myself, loud enough to hear through my ears.<br>
        The only good thing that happened to me during the NEET era was you.<br><br>

        I don't have enough words to express how grateful I am to have you as a friend.<br>
        And because we are kinda two bodies and one soul,<br>
        I need to tell you something:<br>
        Never doubt yourself,<br>
        Never think you're less pretty than anyone (because you're not),<br>
        Never settle for less because of overthinking (because you deserve everything).<br><br>

        And I know me saying this probably won't help when you're surrounded by darkness —<br>
        Because it doesn't, seriously, it doesn't.<br>
        But I want to tell you something I learned throughout my life:<br>
        Life is like clouds — it moves very slowly; sometimes so slowly that it feels like it isn't moving at all.<br>
        Life can sometimes become too difficult to tolerate, and we feel like we'll be stuck here forever.<br>
        But when you take a time-lapse of the clouds, you'll notice they never stopped moving — they were moving with you.<br>
        And in life also, when you look at the time-lapse, you'll realize the difficult moment has already passed.<br>
        And life moves during the happy times too — so enjoy every moment,<br>
        Don't think "I'll do it later." Later never comes.<br><br>

        I won't stretch it too long, cuz you might cry if I start to show my real writing talent 😏<br>
        In short, you're perfect and can achieve everything you want.<br>
        When you're unable to look at the time-lapse, just know I'll always love you no matter what.<br>
        I'd help you bury the body because I'll always support you.<br>
        Learn the guitar, sing songs, and fuck everyone else who makes you feel less (because you're perfect.)<br><br>

        (Scroll down for the last surprise 😚)
        """
        poem = """
        Remember the orchid bracelet,<br>
        the flower symbolising you,<br>
        and the thread tying us.<br><br>

        The butterfly poem you wrote,<br>
        the tissue paper with lipsticks,<br>
        the poem that I treasure.<br><br>

        The silly Q&amp;A we play,<br>
        the dance videos we make —<br>
        not caring about others.<br><br>

        How excited we always are<br>
        to meet after months,<br>
        how excited we always are<br>
        for our photos,<br>
        how the food gets cold<br>
        because our talk doesn't end.<br><br>

        You're like —<br>
        the wish from a fallen star,<br>
        the wish finally answered,<br>
        the wish that completed the fallen star.<br><br>

        We're like —<br>
        the rain and the ocean,<br>
        one falls from the sky —<br>
        and the other catches.<br>
        Together we hold each other.<br>
        """
        col1 ,col2 = st.columns([1,1])
        st.markdown("""
        <style>
        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            max-width: 100% !important;
        }
        </style>
        """, unsafe_allow_html=True)
        with col1:
            st.markdown(f"""
                <div class='card'>{poem}</div>""",unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class='card'>{msg}</div>""",unsafe_allow_html=True)

        if st.button("One Last Surprise🎁"):
            st.session_state.page +=1
            st.rerun()

elif st.session_state.page == 7:
    with page_cont.container():
        st.video(os.path.join("birthday","video.mov"))
        st.markdown("""<div class='love'> Love You Bro❤️</div>""",unsafe_allow_html=True)
        st.markdown("""<div class='happy'> Be Happy Always🫶</div>""",unsafe_allow_html=True)
