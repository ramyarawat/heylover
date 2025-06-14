import streamlit as st

st.set_page_config(page_title="HEY! LOVE💌", page_icon="💖", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #fff0f5;
        }
        h1, h2, h3, p {
            text-align: center;
        }
        .stButton>button {
            background-color: #ff69b4;
            color: white;
            border-radius: 15px;
            height: 3em;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

st.title("HEY! LOVE💌")
st.write("Hi Raghvi! Ramyyyyyy made this for you 💖")

# Question flow using session state
if 'step' not in st.session_state:
    st.session_state.step = 1

if st.session_state.step == 1:
    ans1 = st.text_input("1. What's your ideal way to spend time together? 🥰")
    if st.button("Next ❤️"):
        st.session_state.ans1 = ans1
        st.session_state.step = 2

elif st.session_state.step == 2:
    ans2 = st.radio("2. Will you go on a date with me? 💕", ["Yes", "Maybe", "No"], index=None)
    if st.button("Next 💖"):
        st.session_state.ans2 = ans2
        st.session_state.step = 3

elif st.session_state.step == 3:
    ans3 = st.radio("3. How excited are you to go on a date with me? 😍", ["Very", "Can't wait to see you!"], index=None)
    if st.button("Next 💘"):
        st.session_state.ans3 = ans3
        st.session_state.step = 4

elif st.session_state.step == 4:
    ans4 = st.radio("4. Are you free on 28 June? 📅", ["Yes", "No"], index=None)
    if st.button("Next 💌"):
        st.session_state.ans4 = ans4
        st.session_state.step = 5

elif st.session_state.step == 5:
    ans5 = st.radio("5. Where do you want to go? 📍", ["Majnu Ka Tilla", "Connaught Place", "Somewhere else"], index=None)
    custom_place = ""
    if ans5 == "Somewhere else":
        custom_place = st.text_input("Tell me where you'd like to go! ✨")
    if st.button("Submit 💝"):
        st.session_state.ans5 = ans5
        st.session_state.custom_place = custom_place
        st.session_state.step = 6

elif st.session_state.step == 6:
    st.subheader("Your Answers 💌")
    st.write(f"1️⃣ Ideal time: {st.session_state.ans1}")
    st.write(f"2️⃣ Date answer: {st.session_state.ans2}")
    st.write(f"3️⃣ Excitement: {st.session_state.ans3}")
    st.write(f"4️⃣ Free on 28 June: {st.session_state.ans4}")
    st.write(f"5️⃣ Preferred place: {st.session_state.ans5} {'- ' + st.session_state.custom_place if st.session_state.ans5 == 'Somewhere else' else ''}")

    st.markdown("---")
    if st.session_state.ans2 == "Yes":
        st.success("Yay!! 🎉 I can't wait to spend time with you 🥰")
        st.markdown("""
        💌 **For my cutest boy, Raghvi** 💌  
        I am grateful that you came into my life. You are all the motivation I need, and I love you so much I don’t want to let you go.  
        I’m so in love with you honey 🍯  
        See you soon, kutte 🐶 💖
        """)
    else:
        st.warning("Hmm... I'm still taking you out anyway 😜")
