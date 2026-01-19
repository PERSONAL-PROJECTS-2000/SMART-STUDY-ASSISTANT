import streamlit as SL
from utils.APIs import call_gemini_with_retry

def render():
    SL.markdown("### Chat with AI")
    for message in SL.session_state.chat_history:
        with SL.chat_message(message["role"]):
            SL.write(message["content"])
    user_input = SL.chat_input("Ask me anything...")
    if user_input:
        SL.session_state.chat_history.append({"role": "user", "content": user_input})
        with SL.chat_message("user"):
            SL.write(user_input)
        with SL.chat_message("assistant"):
            response = call_gemini_with_retry(user_input)
            SL.write(response)
            SL.session_state.chat_history.append({"role": "assistant", "content": response})