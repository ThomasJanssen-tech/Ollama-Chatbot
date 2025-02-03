import streamlit as st

# create the input form
prompt = st.chat_input("Say something")

# if input provided, add it to the screen
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        st.markdown(f"You said: {prompt}")