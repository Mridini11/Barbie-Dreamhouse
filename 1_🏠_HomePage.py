import requests
import openai
import streamlit as st
from streamlit_lottie import st_lottie
import time


st.set_page_config(
    page_title="Citizen for Sustainability",
    page_icon="💚"
)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/f8b98070-2828-4e92-9dcb-4725b77101e3/S1Rsj8k9b8.json")
lottie_coding2 = load_lottieurl("https://lottie.host/e16933f1-8888-4b1a-a17d-caa420dc5241/QFYcZQ0xAF.json")
lottie_coding3 = load_lottieurl("https://lottie.host/bd374c86-a624-4693-848c-63a6f986f48e/QOVaEpcC6n.json")

st.image("https://i.ibb.co/yY0DwYS/Screenshot-2023-09-30-134603.png")
st.title("Ready To Become A Citizen for Sustainability? 🌲")
st.sidebar.success("Donate to us!")

if "user_name" not in st.session_state:
    st.session_state["user_name"] = ""

user_name = st.text_input("Enter your name", st.session_state["user_name"])
submit = st.button("Submit")
if submit:
    st.session_state["user_name"] = user_name

if user_name:
    if isinstance(user_name, str):
        st.subheader("Welcome "+ user_name + "!")
    else:
        st.write("**Please enter a valid name.**")
    time.sleep(1.0)
    st.write("Sustainability has become the new norm and we are sure you want to contribute to improve our vibrant community. Following SDG11- Sustainable cities and communities, you can do your part to make the world a better place by joining us as a volunteer. So what are you waiting for, let’s change the world together!")
    st.write("Spend your time advocating for a change with the following volunteering opportunities.")
    time.sleep(0.5)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("**Beach Cleanup by Ocean Purpose Project**")
        st.write("Clean up the beach and 7am to bring people from all walks of life to form a community with a common goal. Through this activity, we want to increase awareness of marine trash in Singapore and how it affects local biodiversity.")
        st.write("When: 10am-12pm, 30th September 2023")
        st.write("Where: At East Coast Park, near Jumbo Seafood")
        st.write("##")
        time.sleep(0.5)
        st.subheader("**Tree Plantations By NParks**")
        st.write("Help us plant 150 trees to restore nature back into our city and achieve our new City in Nature vision. This wil redouble our efforts to green our urban infrastructure on an unprecedented scale. This initiative is in support of the Singapore Green Plan 2030.")
        st.write("When: 2pm-4pm, 20th October 2023")
        st.write("Where: Sungei Buloh Wetland Reserve, Singapore 739453")
        st.write("##")
        time.sleep(0.5)
        st.subheader("**Farm-Work at Ground-Up Initiative**")
        st.write("Help us by lending a hand at our Kampung location, where we nurture a community from the ground-up and grow our own vegetables, fruits, and plants while ensuring we maintain a minimal carbon footprint.")
        st.write("When: 9am-12pm, 30th November 2023")
        st.write("91 Lorong Chencharum Singapore 769201")

    with col2:
        st.write("##")
        st_lottie(lottie_coding, width=320, key="beachcleanup")
        st.button("Join", key="Beach", type="secondary")
        st.write("##")
        st.write("##")
        time.sleep(0.5)
        st_lottie(lottie_coding2, width=320, key="treesgrowth")
        st.button("Join", key="tree", type="secondary")
        st.write("##")
        st.write("##")
        time.sleep(0.5)
        st_lottie(lottie_coding3, width=320, key="farmerboy")
        st.button("Join", key="farm", type="secondary")


custom_css = f"""
    <style>
        .title-text {{
            font-size: 15px; /* Adjust the font size as needed */
        }}
    </style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
st.subheader("Any questions? Ask help from our chatbot! 🤖")


openai.api_key = st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


api_request_count = 0
rate_limit_reset_time = time.time() + 3600  # 1 hour

if st.session_state.get("messages") is None:
    st.session_state.messages = []

prompt = st.chat_input("What is up?")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})


    if api_request_count >= 60 or time.time() >= rate_limit_reset_time:
        st.error("Rate limit exceeded. Please wait a moment before sending another message.")
    else:
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for response in openai.ChatCompletion.create(
                    model=st.session_state["openai_model"],
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True,
            ):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "┃")
                api_request_count += 1

            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})


if time.time() >= rate_limit_reset_time:
    rate_limit_reset_time = time.time() + 3600
