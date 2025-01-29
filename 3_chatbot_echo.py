import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

st.title("Chatbot")

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat messages from history on app rerun
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)
            
# create the bar where we can type messages
prompt = st.chat_input("How are you?")

# did the user submit a prompt?
if prompt:

    # add the message from the user (prompt) to the screen with streamlit
    with st.chat_message("user"):
        st.markdown(prompt)

        st.session_state.messages.append(HumanMessage(prompt))

    # create the echo (response) and add it to the screen
    response = f"Echo: {prompt}"

    with st.chat_message("assistant"):
        st.markdown(response)

        st.session_state.messages.append(AIMessage(response))