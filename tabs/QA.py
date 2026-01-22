import streamlit as SL
from utils.APIs import call_gemini_with_retry
from utils.DOCs import extract_text_from_file

def render_qa():
    SL.markdown("### Generate Answers to Questions")
    SL.write("Get instant answers to your written questions.")
    col1, col2 = SL.columns([2, 1])
    with col1:
        qa_file = SL.file_uploader("Upload Document", type=['txt', 'pdf', 'docx', 'doc', 'pptx', 'jpg', 'jpeg', 'png', 'xlsx'], key="qa_file")
    with col2:
        qa_topic = SL.text_input("Topic Name (Optional)", placeholder="Enter the topic name", key="qa_topic")
    if SL.button("Generate answers", type="primary", key="qa_btn"):
        if qa_file:
            with SL.spinner("Generating answers..."):
                text = extract_text_from_file(qa_file)
                prompt = f"Identify all questions in this document and provide detailed answers"
                if qa_topic:
                    prompt += f" in the context of '{qa_topic}'"
                prompt += f":\n\n{text}"
                result = call_gemini_with_retry(prompt)
                SL.text_area("Questions & Answers", result, height=400, key="qa_output")
        else:

            SL.warning("Please upload a document first!")
