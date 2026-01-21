import streamlit as SL
def apply_theme():
#    if SL.session_state.theme == 'day':
#        SL.markdown("""
#        <style>
#        .stApp {
#            background-color: #f5f5f5;
#            color: #000000;
#        }
#        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
#            background-color: white;
#            color: #000000;
#        }
#        </style>
#        """, unsafe_allow_html=True)
#    else:
#        SL.markdown("""
#        <style>
#        .stApp {
#            background-color: #1a1a1a;
#            color: #e0e0e0;
#        }
#        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
#            background-color: #2d2d2d;
#            color: #e0e0e0;
#        }
#        </style>

#        """, unsafe_allow_html=True)
    common_css = """
    <style>
        /* Requirement 5: Browse Files button text white in BOTH modes */
        section[data-testid="stFileUploader"] button p {
            color: white !important;
        }
        /* Ensure file uploader button background is dark enough to show white text */
        section[data-testid="stFileUploader"] button {
            background-color: #4F4F4F !important;
            border: none !important;
        }
    </style>
    """
    SL.markdown(common_css, unsafe_allow_html=True)

    if SL.session_state.theme == 'day':
        SL.markdown("""
        <style>
            /* Base App Background */
            .stApp {
                background-color: #f5f5f5;
                color: #000000;
            }

            /* Requirement 1: Unselected tab names black */
            button[data-baseweb="tab"] p {
                color: black !important;
            }

            /* Requirement 2: Tab base line and selected highlight black/dark grey */
            [data-baseweb="tab-list"] {
                border-bottom: 2px solid #333333 !important;
            }
            div[data-baseweb="tab-highlight"] {
                background-color: #000000 !important;
            }

            /* Requirement 3: Container box outline (Forms) black/dark grey */
            div[data-testid="stForm"], .stChatMessage {
                border: 1px solid #333333 !important;
                border-radius: 0.5rem;
                padding: 1rem;
            }

            /* Requirement 4: User input field names (Labels) black */
            label[data-testid="stWidgetLabel"] p {
                color: black !important;
                font-weight: 600 !important;
            }

            /* Requirement 5 & 7: Placeholder text dark grey */
            input::placeholder, textarea::placeholder {
                color: #555555 !important;
                opacity: 1;
            }

            /* Sidebar specific placeholders */
            [data-testid="stSidebar"] input::placeholder {
                color: #555555 !important;
            }

            /* Requirement 6: Output container contrast (Day Mode) */
            /* Making text areas and markdown outputs clear */
            .stTextArea textarea {
                background-color: #ffffff !important;
                color: #000000 !important;
                border: 1px solid #cccccc !important;
            }
            div[data-testid="stMarkdownContainer"] {
                color: #000000 !important;
            }
        </style>
        """, unsafe_allow_html=True)
    else:
        # NIGHT MODE
        SL.markdown("""
        <style>
            /* Base App Background */
            .stApp {
                background-color: #1a1a1a;
                color: #e0e0e0;
            }

            /* Input fields in Night Mode */
            .stTextInput>div>div>input, .stTextArea>div>div>textarea {
                background-color: #2d2d2d;
                color: #e0e0e0;
                border: 1px solid #444444;
            }

            /* Requirement 6: Output container contrast (Night Mode) */
            .stTextArea textarea {
                background-color: #2d2d2d !important;
                color: #e0e0e0 !important;
            }
            
            /* Tab text in Night Mode for visibility */
            button[data-baseweb="tab"] p {
                color: #e0e0e0 !important;
            }
            div[data-baseweb="tab-highlight"] {
                background-color: #e0e0e0 !important;
            }
        </style>
        """, unsafe_allow_html=True)
