# Function: Rule-based bot responses

import streamlit as st
st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")
# st.set_page_config(page_title="Chatbot", page_icon="💬", layout="centered")

st.title("Simple Streamlit Chatbot")

# Initialize session state 
if "messages" not in st.session_state:
    st.session_state["messages"] = []

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I’m a  Streamlit Chatbot."
    elif "bye" in user_input:
        return "Goodbye! Have a great day."
    elif "help" in user_input:
        return "Sure! You can ask me about my features or just chat casually."
    else:
        return "I'm not sure how to answer that, but I'm learning!"

# User input
user_input = st.text_input("Type your message here:", "")

if st.button("Send") and user_input:
    # user message
    st.session_state["messages"].append(("You", user_input))
    # bot response
    bot_reply = chatbot_response(user_input)
    st.session_state["messages"].append(("Bot", bot_reply))

# Display conversation
st.header("Conversation:")
for sender, msg in st.session_state["messages"]:
    st.markdown(f"**{sender}:** {msg}")