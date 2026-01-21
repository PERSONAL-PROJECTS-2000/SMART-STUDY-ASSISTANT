import streamlit as SL
def apth():
    if SL.session_state.theme == 'day':
        SL.markdown("""
        <style>
        .stApp {
            background-color: #f5f5f5;
            color: #000000;
        }
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            background-color: white;
            color: #000000;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        SL.markdown("""
        <style>
        .stApp {
            background-color: #1a1a1a;
            color: #e0e0e0;
        }
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            background-color: #2d2d2d;
            color: #e0e0e0;
        }
        </style>

        """, unsafe_allow_html=True)
