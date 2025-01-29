import streamlit as st

# create the input form
prompt = st.chat_input("Say something")

# if input provided, add it to the screen
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")