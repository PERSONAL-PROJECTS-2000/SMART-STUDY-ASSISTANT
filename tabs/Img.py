import streamlit as SL
from utils.APIs import call_gemini_with_retry
from utils.DOCs import extract_text_from_file

def render_image_search():
    SL.markdown("### Find Relevant Images")
    col1, col2 = SL.columns([2, 1])
    with col1:
        img_file = SL.file_uploader("Upload Document", type=['txt', 'pdf', 'docx', 'doc', 'pptx', 'jpg', 'jpeg', 'png', 'xlsx'], key="img_file")
    with col2:
        img_topic = SL.text_input("Topic Name (Optional)", placeholder="Enter the topic name", key="img_topic")
    if SL.button("Find image", type="primary", key="img_btn"):
        if img_file:
            with SL.spinner("Searching for images..."):
                text = extract_text_from_file(img_file)[:200]
                prompt = f"Search the web for an image that matches this description: {text}"
                if img_topic:
                    prompt += f" related to '{img_topic}'"
                prompt += "\n\nProvide the image link and description."
                result = call_gemini_with_retry(prompt)
                SL.text_area("Image Results", result, height=400, key="img_output")
        else:
            SL.warning("Please upload a document first!")