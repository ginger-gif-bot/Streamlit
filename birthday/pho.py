import os
import streamlit as st
# count = 0
# folder = r"D:\streamlit\birthday\photos"
# for file_name in os.listdir(folder):
#     old_path = os.path.join(folder,file_name)
#     print(old_path)
#     if os.path.isfile(old_path) and file_name.startswith("Wh"):
#         new_path = os.path.join(folder,f"photo_{count}.jpeg")
#         os.rename(old_path,new_path)
#         count +=1
# print("done")

# folder = r"birthday\photos"
# files = os.listdir(folder)
# row_1 = files[:13]
# row_2 = files[13:27]
# row_3 = files[27:]
# print(len(row_1))
# print(len(row_2))
# print(len(row_3))

# <h4 style='margin-top:0px'> 🎀❤️🎊🎉🎈❤️🎀</h4>
style = os.path.join("birthday","style.css")
with open(style) as f:
     st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

# st.markdown(f"""
#     <div class='bday'>HAPPY BIRTHDAY</div>
#     <div class='name'>Snehal</div>
#  """,unsafe_allow_html=True)
# col1 ,  col2, col_empty = st.columns([1,1,1])
# with col1:
#     st.markdown(f"""
#         <div class='card'>poem
#         </div>
#     """,unsafe_allow_html=True)
# with col2:
#     st.markdown(f"""
#         <div class='card'>msg
#         </div>
#     """,unsafe_allow_html=True)

# with col_empty:
#     st.markdown("""
#     <style>
#     .stButton button {
#         font-size: 10px !important;
#         font-weignt: 400px !important;
#         margin: -9px !important;
#         padding: 6px 18px !important;
#         border-radius: 20px !important;
#         background: radial-gradient(#310007,#78463a,#BC8F8F) !important;
#         color: #e6ceaf !important;
#     }
#     </style>
#     """, unsafe_allow_html=True)
#     if st.button("One Last Surprise🎁"):
#         st.session_state.page +=1
#         st.rerun()

# with page_cont.container():
# st.markdown("""
#         <style>
#         .block-container { padding: 0 !important;}
#         iframe { width: 100% !important; height: 90vh !important;}
#         .stVideo {
#         padding: 0 !important;
#         margin: 0 !important;
#         width: 100% !important;
#     }

#     .stVideo > div {
#         padding: 0 !important;
#         width: 100% !important;
#     }
#         </style>""",unsafe_allow_html=True)


# st.video(os.path.join("birthday","video.mov"))
# st.markdown("""<div class='love'> Love You Bro❤️</div>""",unsafe_allow_html=True)
# st.markdown("""<div class='happy'> Be Happy Always🫶</div>""",unsafe_allow_html=True)

# """
# dear Snehal,
# once, when the stars fell from the cradle of lonliness
# i made a wish, to find a friend who can be the twin of me
# perhaps the stars listened to me coz i got you.

# i have friends, but no one like you.
# when i speak to you there's a different kind of comfort like after a long
# time i am speaking to myself, loud enough to hear through my years.
# only good thing that happened to me during the NEET era was you.

# i dont have enough words to express how grateful i am to have you as a friend.
# and beacuse we are kinda two bodies and one soul;
# i need to tell you something:
# never doubt yourself,
# never think you're less pretty than anyone(coz you're not),
# never settle for less because of overthinking (coz you desereve everything),

# and i know me saying this propably won't help when you're surrounded by darkness
# coz it doesn't, seroiusly it doesn't.
# but i want to tell you something which i learned throughout my life:
# life is like clouds- it moves very slowly; that sometimes it feels like it isn't moving at all.
# life sometimes can become, too difficult to tolerate that we feel like we're not moving and will stay stuck here forever.
# but when you take timelapse of the clouds, you'll notice it never stopped moving-it was moving with you.
# and in life also, when you'll look at the time lapse you'll realise, the difficult moment already passed.
# and life also moves during the happy time- so enjoy every moment in your life,
# don't think that I'll do it later. later never comes.

# i won't strech it too long, cuz you might cry if i start to show my real writing talent😏.
# in short, you're perfect and can achieve everything you want.
# when you're unable to look at the timelapse, just know I'll always love you no matter what.
# i help you bury the body because I'll always support you.
# learn the guitar, sing songs and fuck everyone else who make you feel less(coz you're perfect.)
# (scroll down for the last surprise😚)
# """

# """
# like the stars once fell,
# from the cradle of lonliness,
# i wished for a friend,
# i wished for a wave of happiness.

# somehow, the stars that-
# never listened to anyone,
# listened to me-
# and i got you as my twin.

# you are like-
# the sun that everyone wishes
# in the cold winter.
# like the sunlight peeking under the ocean.
# like the moonlight in the pitch black night.

# and i wish that-
# our friendship brings happiness and peace to us.
# lets always shine brightly 
# like the stars
# lets always look towards the sun
# like the wildflowers.
# lets be happy.
# """

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
    Like the stars once fell,<br>
    from the cradle of loneliness,<br>
    I wished for a friend,<br>
    I wished for a wave of happiness.<br><br>

    Somehow, the stars that<br>
    never listened to anyone,<br>
    listened to me —<br>
    and I got you as my twin.<br><br>

    You are like<br>
    the sun that everyone wishes for<br>
    in the cold winter,<br>
    like the sunlight peeking under the ocean,<br>
    like the moonlight in the pitch black night.<br><br>

    And I wish that<br>
    our friendship brings happiness and peace to us.<br>
    Let's always shine brightly<br>
    like the stars,<br>
    let's always look towards the sun<br>
    like the wildflowers.<br>
    Let's be happy.<br>
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