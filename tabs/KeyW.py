import streamlit as SL
from utils.APIs import call_gemini_with_retry
from utils.DOCs import extract_text_from_file

def render_keywords():
    SL.markdown("### Find and Explain Key Words")
    col1, col2 = SL.columns([2, 1])
    with col1:
        kw_file = SL.file_uploader("Upload Document", type=['txt', 'pdf', 'docx', 'doc', 'pptx', 'jpg', 'jpeg', 'png', 'xlsx'], key="kw_file")
    with col2:
        kw_topic = SL.text_input("Topic Name (Optional)", placeholder="Enter the topic name", key="kw_topic")
    if SL.button("Find and explain key words", type="primary", key="kw_btn"):
        if kw_file:
            with SL.spinner("Finding keywords..."):
                text = extract_text_from_file(kw_file)
                prompt = f"Identify all key terms/keywords from this document"
                if kw_topic:
                    prompt += f" related to '{kw_topic}'"
                prompt += f", and explain each one with examples:\n\n{text}"
                result = call_gemini_with_retry(prompt)
                SL.text_area("Keywords & Explanations", result, height=400, key="kw_output")
        else:
            SL.warning("Please upload a document first!")