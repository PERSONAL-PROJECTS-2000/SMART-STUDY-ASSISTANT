import streamlit as SL
#from utils.Theme import apply_theme as apth
from tabs.Chat import render as cren
from tabs.Summ import render_summarize as smren
from tabs.Exp import render_explain as exren
from tabs.KeyW import render_keywords as kwren
from tabs.Sim import render_similar as sren
from tabs.Links import render_links as lren
from tabs.Img import render_image_search as iren
from tabs.QA import render_qa as qaren
from tabs.TimTab import rendert as tren
from tabs.HowToUse import usage as use

SL.set_page_config(page_title="AI-powered Smart Study Assistant", page_icon="🎓", layout="wide", initial_sidebar_state="expanded")

if 'api_keys' not in SL.session_state:
    SL.session_state.api_keys = []
if 'current_key_index' not in SL.session_state:
    SL.session_state.current_key_index = 0
#if 'theme' not in SL.session_state:
    #SL.session_state.theme = 'day'
if 'tasks' not in SL.session_state:
    SL.session_state.tasks = []
if 'chat_history' not in SL.session_state:
    SL.session_state.chat_history = []
if 'client' not in SL.session_state:
    SL.session_state.client = None

with SL.sidebar:
    SL.markdown("### 🔑 API Configuration")
    api_key_inputs = []
    for i in range(10):
        key = SL.text_input(f"API Key {i+1}", type="password", key=f"api_key_{i}", placeholder=f"Enter Gemini API key ({i+1})")
        if key:
            api_key_inputs.append(key)
    if SL.button("Load API Keys"):
        SL.session_state.api_keys = [k.strip() for k in api_key_inputs if k.strip()]
        SL.session_state.current_key_index = 0
        SL.success(f"Loaded {len(SL.session_state.api_keys)} API key(s)")

SL.title("🎓 AI-powered Smart Study Assistant")
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10  = SL.tabs(["💬 Chat","📝 Summarize","📚 Explain","🔑 Key Words","🔍 Similar Content","🌐 Web Links","❓ Q&A","🖼️ Image Search","📅 Timetable","ℹ️ How To Use"])

with tab1:
    cren()
with tab2:
    smren()
with tab3:
    exren()
with tab4:
    kwren()
with tab5:
    sren()
with tab6:
    lren()
with tab7:
    qaren()
with tab8:
    iren()
with tab9:
    tren()
with tab10:
    use()

