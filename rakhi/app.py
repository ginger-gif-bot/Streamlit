import streamlit as st
import time
st.set_page_config(page_title="RakshaBandhan",layout="wide")  

st.markdown("""
<style>
header[data-testid="stHeader"] {
display: None;
}
.stApp {
    background: radial-gradient(ellipse at center,
    #F4A0B5 0%,
    #FADADD 60%,
    #B06080 100%);
}
.stApp{
text-align: center;
}
h2 {
    font-size: 3.5rem !important;
}
* {
    color: #8B1A4A !important;
}
.block-container {
    max-width: 100% !important;
    padding: 0rem 4rem !important;
}
.stTextInput label {
    width:100%;
    text-align: center;
    color: #8B1A4A !important;
}
.stTextInput input,
.stTextInput input:focus,
.stTextInput input:active,
.stTextInput input:hover {
    background-color: #FFE0E8 !important;
    border-radius: 20px !important;
    border: 2px solid #C47090 !important;
    box-shadow: none !important;
    outline: none !important;
    color: #8B1A4A !important;
    font-size: 1.3rem !important;
    text-align: center !important;
}
.stTextInput {
    margin-top: -30px;
}
.stImage img {
    max-height: 75vh !important;
    object-fit: cover !important;
    width: 100% !important;
}
div[data-testid="stHorizontalBlock"] {
    gap: 0px !important;
}
div[data-testid="stImage"] img {
    height: 70vh !important;
    width: 100% !important;
    object-fit: cover !important;
    display: block !important;
}
.card {
    background: rgba(255,255,255,0.3);
    border-radius: 20px;
    padding: 15px;
    font-size: 0.95rem;
    line-height: 1.5;
    text-align: center;
}
</style>
""",unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Welcome"
if "name" not in st.session_state:
    st.session_state.name = ""

if st.session_state["page"] == "Welcome":
    st.markdown("<h1 style='text-align:center;'>❤️🎀Happy Raksha Bandhan!❤️🎀</h1>",unsafe_allow_html=True)
    st.markdown("<div style='margin-bottom:40px;',</div>",unsafe_allow_html=True)
    st.markdown("<h3 style='margin-left:5%;'>A festival I couldn't have been able to celebrate without you two.</h3>",unsafe_allow_html=True)
    st.markdown("<h4 style='margin-left:7%;'>May we bicker and love forever!!😘</h4>",unsafe_allow_html=True)
    col1, col2, col3= st.columns([1,1,1])
    with col2:
        st.markdown("<h4 style='text-align:center; color:#8B1A4A;'>Which one of you it is now:</h4>",unsafe_allow_html=True)
        name = st.text_input(" ",label_visibility="hidden").capitalize()
    if name:
        st.session_state.name = name
        st.session_state.page = "Slideshow"
        st.balloons()
        st.rerun()

    st.markdown("<div style='margin-bottom:20px;'</div>",unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>❤️❤️❤️I love you both so much.❤️❤️❤️</h2>",unsafe_allow_html=True)

elif st.session_state.page == "Slideshow":
    photos = {"Aryan":["rakhi/a1.jpeg","rakhi/ak.jpeg","rakhi/a2.jpeg"],
              "Hardik":["rakhi/h1.jpeg","rakhi/hk.jpeg","rakhi/h2.jpeg"]}   
    name = st.session_state.name
    st.subheader(f"Hello, {name}")
    person_photos = photos.get(name,[]) 
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        ph1 = st.empty()
    with col2:
        ph2 = st.empty()
    with col3:
            ph3 = st.empty()
    placeholders = [ph1,ph2,ph3]
    for i, photo in enumerate(person_photos):
        placeholders[i].image(photo,use_container_width=True)
        time.sleep(1)

    time.sleep(1)
    st.session_state.page = "message"
    st.rerun()

elif st.session_state.page == "message":
    st.balloons()
    name = st.session_state.name

    poem = """
    With the Rakhi I tie every year,<br>
    With your promise to protect me,<br>
    And mine to be your—<br>
    Elder sister,<br>
    Mother,<br>
    Your Best Friend.<br><br>
    This bond of ours—<br>
    Pure, innocent and beautiful,<br>
    Will always be above every relation.<br>
    No matter how old you grow,<br>
    No matter how annoying you get,<br>
    You'll always be loved by me.<br><br>
    And don't worry,<br>
    I'll talk to papa<br>
    About your share in the property 😌<br>
    Let's stay together, always.<br>
    Now, where's my gift? 😤
    """

    personal = {
            "Hardik": """I may not be the smartest, kindest, or funniest sister for you.<br>
        But I love you in my own way, very much.<br>
        Sometimes you do nothing and just talk to me, but I get annoyed — I don't know why.<br>
        When you treat me like I'm the younger one, I want to kill you.<br>
        Basically, I've wanted to kill you almost all the time.<br>
        But I've been tolerating you since you were born, and now I can't imagine my life without you.<br>
        Let's always bicker and reconcile over food and our own goofy jokes.<br>
        Which year am I going to get my gift, huh?<br><br>
        You've supported me, believed in me, loved me when I couldn't love myself.<br>
        I don't know what I would've done without you two.<br>
        At last, I just want to say that I love you, and always will.<br>
        I will always support your dreams.<br>
        Just always know that your elder (sometimes younger) sister will be there for you.<br>
        — Kiran 🧡""",

            "Aryan": """I may not be the smartest, kindest, or funniest sister for you.<br>
        But I love you in my own way, very much.<br>
        What to say — you're the best person I have in this house, my ultimate support.<br>
        You pamper me like I'm the younger one, make me feel loved.<br>
        You give me your food — even when I don't give you mine.<br>
        You motivate me, spoil me with your little precious gifts,<br>
        give me money when I'm the one who should be giving you money.<br>
        You see, it's like you're the elder brother and I'm the youngest.<br><br>
        You've supported me, believed in me, loved me when I couldn't love myself.<br>
        I don't know what I would've done without you two.<br>
        At last, I just want to say that I love you, and always will.<br>
        I will always support your dreams.<br>
        Just always know that your elder (sometimes younger) sister will be there for you.<br>
        — Kiran 🧡"""
    }

    st.markdown(f"<h3 style='text-align:center;'>🎊 Dear {name}! 🎊</h1>",
                unsafe_allow_html=True)

    col1,gap, col2 = st.columns([1,0.05,1])

    with col1:
        st.markdown(f'<div class="card">{poem}</div>', 
                unsafe_allow_html=True)

    with col2:
        msg = personal.get(name, "Happy Raksha Bandhan! 🎀")
        st.markdown(f'<div class="card">{msg}</div>', 
                unsafe_allow_html=True)

