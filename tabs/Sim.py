import streamlit as SL
import os
from utils.APIs import call_gemini_with_retry
from utils.DOCs import extract_text_from_file

def render_similar():
    SL.markdown("### Find Similar Documents/Images")
    SL.write("Use the AI as an automatic web search tool to find a similar document/image.")
    col1, col2 = SL.columns([2, 1])
    with col1:
        sim_file = SL.file_uploader("Upload Document", type=['txt', 'pdf', 'docx', 'doc', 'pptx', 'jpg', 'jpeg', 'png', 'xlsx'], key="sim_file")
    with col2:
        sim_topic = SL.text_input("Topic Name (Optional)", placeholder="Enter the topic name", key="sim_topic")
    if SL.button("Find similar document/image", type="primary", key="sim_btn"):
        if sim_file:
            with SL.spinner("Searching for similar content..."):
                text = extract_text_from_file(sim_file)[:500]
                file_ext = os.path.splitext(sim_file.name)[1].lower()
                search_type = "similar image" if file_ext in ['.jpg', '.jpeg', '.png'] else "similar document or article"
                prompt = f"Search the web for a {search_type} containing information about: {text}"
                if sim_topic:
                    prompt += f" related to '{sim_topic}'"
                prompt += "\n\nProvide the link and a brief description."
                result = call_gemini_with_retry(prompt)
                SL.text_area("Similar Content", result, height=400, key="sim_output")
        else:

            SL.warning("Please upload a document first!")
