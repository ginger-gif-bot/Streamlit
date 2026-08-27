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

    st.markdown("<div style='margin-bottom:20px;',</div>",unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>❤️❤️❤️I love you both so much.❤️❤️❤️</h2>",unsafe_allow_html=True)

elif st.session_state.page == "Slideshow":
    photos = {"Aryan":["a1.jpeg","ak.jpeg","a2.jpeg"],
              "Hardik":["h1.jpeg","hk.jpeg","h2.jpeg"]}   
    name = st.session_state.name
    st.subheader(f"Hello, {name}")
    person_photos = photos.get(name,[]) 
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        ph1 = st.empty()
    with col2:
        # st.markdown("<div style='margin-top:40px;',</div>",unsafe_allow_html=True)
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
    messages = {
        "Hardik": "HArdiiiikkk",
        "Aryan": "ARRRyyyana"
    }
    msg = messages.get(name,"Happy Raksha Bandhan!")
    st.markdown(f"<h1 style='text-align:left;'>Dear {name}, </h1>",unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:left;'>{msg}</h3>",unsafe_allow_html=True)