import streamlit as SL
from utils.APIs import call_gemini_with_retry
from utils.DOCs import extract_text_from_file

def render_summarize():
    SL.markdown("### Summarize Your Document")
    col1, col2 = SL.columns([2, 1])
    with col1:
        sum_file = SL.file_uploader("Upload Document", type=['txt', 'pdf', 'docx', 'doc', 'pptx', 'jpg', 'jpeg', 'png', 'xlsx'], key="sum_file")
    with col2:
        sum_topic = SL.text_input("Topic Name (Optional)", placeholder="Enter the topic name", key="sum_topic")
    if SL.button("Summarize", type="primary", key="sum_btn"):
        if sum_file:
            with SL.spinner("Generating summary..."):
                text = extract_text_from_file(sum_file)
                prompt = f"Summarize the following document"
                if sum_topic:
                    prompt += f" focusing on the topic '{sum_topic}'"
                prompt += f":\n\n{text}"
                result = call_gemini_with_retry(prompt)
                SL.text_area("Summary", result, height=400, key="sum_output")
        else:
            SL.warning("Please upload a document first!")