import streamlit as SL
from utils.Theme import apply_theme
from tabs import Chat, Summ, Exp, KeyW, Sim, Links, QA, Img, TimTab

SL.set_page_config(
    page_title="AI-powered Smart Study Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

if 'api_keys' not in SL.session_state:
    SL.session_state.api_keys = []
if 'current_key_index' not in SL.session_state:
    SL.session_state.current_key_index = 0
if 'theme' not in SL.session_state:
    SL.session_state.theme = 'day'
if 'tasks' not in SL.session_state:
    SL.session_state.tasks = []
if 'chat_history' not in SL.session_state:
    SL.session_state.chat_history = []
if 'client' not in SL.session_state:
    SL.session_state.client = None

apply_theme()

with SL.sidebar:
    SL.markdown("### 🔑 API Configuration")
    api_key_inputs = []
    for i in range(10):
        key = SL.text_input(f"API Key {i+1}", type="password", key=f"api_key_{i}", placeholder="Enter Gemini API key")
        if key:
            api_key_inputs.append(key)
    if SL.button("Load API Keys"):
        SL.session_state.api_keys = [k.strip() for k in api_key_inputs if k.strip()]
        SL.session_state.current_key_index = 0
        SL.success(f"Loaded {len(SL.session_state.api_keys)} API key(s)")
    SL.markdown("---")
    SL.markdown("### 🎨 Theme")
    col1, col2 = SL.columns(2)
    with col1:
        if SL.button("☀️ Day"):
            SL.session_state.theme = 'day'
            SL.rerun()
    with col2:
        if SL.button("🌙 Night"):
            SL.session_state.theme = 'night'
            SL.rerun()

SL.title("AI Study Assistant")
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = SL.tabs(["💬 Chat","📝 Summarize","📚 Explain","🔑 Key Words","🔍 Similar Content","🌐 Web Links","❓ Q&A","🖼️ Image Search","📅 Timetable"])

with tab1:
    Chat.render()
with tab2:
    Summ.render_summarize()
with tab3:
    Exp.render_explain()
with tab4:
    KeyW.render_keywords()
with tab5:
    Sim.render_similar()
with tab6:
    Links.render_links()
with tab7:
    QA.render_qa()
with tab8:
    Img.render_image_search()
with tab9:
    TimTab.render()