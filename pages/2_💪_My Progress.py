import streamlit as st
import time

st.image("https://i.ibb.co/0t3qMFk/image.png")
st.title(st.session_state["user_name"] + "'s Progress")

tab1, tab2, tab3 = st.tabs(["SDG Hour Tracker", "Total Progress", "Community Feed"])

with tab1:
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        st.image("https://i.ibb.co/PGxD6K1/image.png")
        st.subheader("SDG 13 - Climate Action")
        st.write("**80 hours out of 100**")
    with col2:
        st.image("https://i.ibb.co/mG8NHC0/image.png")
        st.subheader("SDG 14 - Life Under Water")
        st.write("**60 hours out of 100**")
    with col3:
        st.image("https://i.ibb.co/7bYhCtf/image.png")
        st.subheader("SDG 15 - Life On Land")
        st.write("**40 hours out of 100**")

with tab2:
    col1, col2, col3 = st.columns(gap="small", spec=[0.3, 0.4, 0.3])
    with col2:
        st.image("https://i.ibb.co/Jz6q2hn/image.png")
        st.subheader("**SDG11 - Sustainable Cities and Growth**")
        st.write("**180 hours out of 300**")

with tab3:
    st.image("https://i.ibb.co/cXMD1kg/image.png")
    if "the_input" not in st.session_state:
        st.session_state["the_input"] = ""
    the_input = st.text_input("Type in your comments here", st.session_state["the_input"])
    submit = st.button("Enter")
