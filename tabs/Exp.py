import streamlit as SL
from utils.APIs import call_gemini_with_retry
from utils.DOCs import extract_text_from_file

def render_explain():
    SL.markdown("### Explain Document Content")
    col1, col2 = SL.columns([2, 1])
    with col1:
        exp_file = SL.file_uploader("Upload Document", type=['txt', 'pdf', 'docx', 'doc', 'pptx', 'jpg', 'jpeg', 'png', 'xlsx'], key="exp_file")
    with col2:
        exp_topic = SL.text_input("Topic Name (Optional)", placeholder="Enter the topic name", key="exp_topic")
    SL.markdown("**Select Difficulty Level:**")
    col1, col2, col3 = SL.columns(3)
    levels = [("beginner", col1, "exp_beg"), ("intermediate", col2, "exp_int"), ("advanced", col3, "exp_adv")]
    for level, col, key in levels:
        with col:
            if SL.button(f"Explain for {level} level", type="primary", use_container_width=True, key=f"btn_{key}"):
                if exp_file:
                    with SL.spinner("Generating explanation..."):
                        text = extract_text_from_file(exp_file)
                        prompt = f"Explain the following document at a {level} level"
                        if exp_topic:
                            prompt += f" focusing on the topic '{exp_topic}'"
                        prompt += f":\n\n{text}"
                        result = call_gemini_with_retry(prompt)
                        SL.text_area("Explanation", result, height=400, key=key)
                else:
                    SL.warning("Please upload a document first!")