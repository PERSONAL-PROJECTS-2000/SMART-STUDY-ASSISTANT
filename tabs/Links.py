import streamlit as SL
from utils.APIs import call_gemini_with_retry
from utils.DOCs import extract_text_from_file

def render_links():
    SL.markdown("### Find Related Web Resources")
    SL.write("Get links to relevant and useful sources of information.")
    col1, col2 = SL.columns([2, 1])
    with col1:
        link_file = SL.file_uploader("Upload Document", type=['txt', 'pdf', 'docx', 'doc', 'pptx', 'jpg', 'jpeg', 'png', 'xlsx'], key="link_file")
    with col2:
        link_topic = SL.text_input("Topic Name (Optional)", placeholder="Enter the topic name", key="link_topic")
    if SL.button("Find links", type="primary", key="link_btn"):
        if link_file:
            with SL.spinner("Searching for web links..."):
                text = extract_text_from_file(link_file)[:300]
                prompt = f"Search the web and provide at least 5 links to documentation or information sources about: {text}"
                if link_topic:
                    prompt += f" focusing on '{link_topic}'"
                result = call_gemini_with_retry(prompt)
                SL.text_area("Web Links", result, height=400, key="link_output")
        else:

            SL.warning("Please upload a document first!")
