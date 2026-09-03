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
# """,unsafe_allow_html=True)
col1 ,  col2, col_empty = st.columns([1,1,1])
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

with col_empty:
    st.markdown("""
    <style>
    .stButton button {
        font-size: 10px !important;
        font-weignt: 400px !important;
        margin: -9px !important;
        padding: 6px 18px !important;
        border-radius: 20px !important;
        background: radial-gradient(#310007,#78463a,#BC8F8F) !important;
        color: #e6ceaf !important;
    }
    </style>
    """, unsafe_allow_html=True)
    if st.button("One Last Surprise🎁"):
        st.session_state.page +=1
        st.rerun()
