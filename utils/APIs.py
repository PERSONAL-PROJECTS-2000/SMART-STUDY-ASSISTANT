import google.generativeai as genai
import streamlit as SL

class APIKeyManager:
    @staticmethod
    def get_current_key():
        if not SL.session_state.api_keys:
            return None
        return SL.session_state.api_keys[SL.session_state.current_key_index]
    @staticmethod
    def rotate_key():
        if len(SL.session_state.api_keys) > 1:
            SL.session_state.current_key_index = (SL.session_state.current_key_index + 1) % len(SL.session_state.api_keys)
            return True
        return False

def configure_gemini():
    key = APIKeyManager.get_current_key()
    if not key:
        return None
    try:
        genai.configure(api_key=key)
        model = genai.GenerativeModel('gemini-2.5-flash-lite') 
        SL.session_state.client = model
        return model
    except Exception:
        return None
def call_gemini_with_retry(prompt, max_retries=None):
    if not SL.session_state.api_keys:
        return "Please configure at least one API key in the sidebar."
    if max_retries is None:
        max_retries = len(SL.session_state.api_keys)
    last_error = "Unknown error"
    for attempt in range(max_retries):
        client = configure_gemini()
        if not client:
            return "Failed to configure Gemini client. Check your API keys."
        try:
            response = client.generate_content(prompt)
            return response.text
        except Exception as e:
            last_error = str(e)
            error_str = last_error.lower()
            if APIKeyManager.rotate_key():
                continue 
            else:
                break
    if "quota" in last_error.lower() or "limit" in last_error.lower():
        return f"All API keys exhausted (Quota reached). Last error: {last_error}"
    else:
        return f"Error after trying available keys: {last_error}"

