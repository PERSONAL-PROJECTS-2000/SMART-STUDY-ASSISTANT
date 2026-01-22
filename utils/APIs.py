'''
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
    if key:
        try:
            genai.configure(api_key=key)
            model = genai.GenerativeModel('gemini-2.0-flash')
            SL.session_state.client = model
            return model
        except Exception as e:
            return None
    return None
def call_gemini_with_retry(prompt, max_retries=None):
    if max_retries is None:
        max_retries = max(len(SL.session_state.api_keys), 1)
    for attempt in range(max_retries):
        try:
            client = configure_gemini()
            if not client:
                return "Please configure at least one API key in the sidebar."
            response = client.generate_content(prompt)
            return response.text
        except Exception as e:
            error_str = str(e).lower()
            if "quota" in error_str or "limit" in error_str or "resource_exhausted" in error_str:
                if APIKeyManager.rotate_key():
                    continue
            if attempt == max_retries - 1:
                return f"Error: {str(e)}"
    return "All API keys exhausted. Please add more keys or try later."
'''
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
        # Re-initialize the model to ensure it uses the newly configured key
        model = genai.GenerativeModel('gemini-1.5-flash') 
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
            
            # If we have more keys, rotate and try the next one
            if APIKeyManager.rotate_key():
                continue 
            else:
                # If only one key exists, break the loop to return the error
                break

    # If we get here, it means all retries failed
    if "quota" in last_error.lower() or "limit" in last_error.lower():
        return f"All API keys exhausted (Quota reached). Last error: {last_error}"
    else:
        return f"Error after trying available keys: {last_error}"
