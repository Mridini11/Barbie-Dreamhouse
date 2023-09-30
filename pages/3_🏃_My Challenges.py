import streamlit as st


st.title(st.session_state["user_name"] + "'s Challenges")

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.subheader("**100kgs Trash Challenge**")
    st.image("https://i.ibb.co/7JfXXQ8/Screenshot-2023-09-30-130232.png", width=300)
    st.write("Race to be the first one to collect 100kgs of trash from our beaches and restore back our blue seas and yellow sands. Can't wait to see you on the leaderboard!")
    st.subheader("**200 Trees Planted Challenge**")
    st.image("https://i.ibb.co/hK5r8Mp/TREES.png", width=300)
    st.write("Race to be the first one to plant 200 trees and fulfill your part to uplift the greenery of our community and help mitigate air pollution. Can't wait to see you on the leaderboard! ")
    st.subheader("**50 Hours Farming Challenge**")
    st.image("https://i.ibb.co/hfLm7FH/Screenshot-2023-09-30-130254.png", width=300)
    st.write("Race to be the first one to complete 50 hours of farming, grow your own veggies, and eat fresh! Make us more independent and decrease your carbon footprint. After completing 100 hours, reward yourself with $10 NTUC vouchers.Can't wait to see you on the leaderboard!")

with col2:
    st.subheader("Challenges Leaderboard")
    st.image("https://i.ibb.co/zS34w6X/Screenshot-2023-09-30-134120.png")
    st.write("##")
    st.write("##")
    st.image("https://i.ibb.co/G2dQTps/image.png")
    st.write("##")
    st.write("##")
    st.image("https://i.ibb.co/6NT0ZRn/image.png")
