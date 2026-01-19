# SMART-STUDY-ASSISTANT

# 🎓 AI-Powered Smart Study Assistant

An intelligent study assistant built with Streamlit and Google Gemini AI that helps students with document analysis, summarization, explanations, and study planning.

## ✨ Features

- 💬 **AI Chat** - Ask questions and get intelligent responses
- 📝 **Document Summarization** - Summarize PDFs, Word docs, PowerPoints, and more
- 📚 **Smart Explanations** - Explain content at beginner, intermediate, or advanced levels
- 🔑 **Keyword Extraction** - Find and explain key terms automatically
- 🔍 **Similar Content Finder** - Search for related documents and images
- 🌐 **Web Resource Discovery** - Find relevant online resources
- ❓ **Q&A Generation** - Answer questions from documents
- 🖼️ **Image Search** - Find relevant images based on descriptions
- 📅 **Timetable Generator** - Create personalized study schedules

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Tesseract OCR
- Poppler (for PDF processing)

### Step 1: Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/AI-Study-Assistant.git
cd AI-Study-Assistant
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

Activate it:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### Step 3: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Install Tesseract OCR

**Windows:**
1. Download from: https://github.com/UB-Mannheim/tesseract/wiki
2. Install to: `C:\Program Files\Tesseract-OCR`
3. Add to PATH

**Mac:**
```bash
brew install tesseract
```

**Linux:**
```bash
sudo apt-get install tesseract-ocr
```

### Step 5: Install Poppler

**Windows:**
1. Download from: https://github.com/oschwartz10612/poppler-windows/releases/
2. Extract to: `C:\poppler`
3. Add `C:\poppler\Library\bin` to PATH

**Mac:**
```bash
brew install poppler
```

**Linux:**
```bash
sudo apt-get install poppler-utils
```

## 🚀 Usage

### Step 1: Add Your API Key

Create `.streamlit/secrets.toml` and add your Gemini API key:
```toml
[api_keys]
key1 = "YOUR_GEMINI_API_KEY_HERE"
```

Get your free API key from: https://makersuite.google.com/app/apikey

### Step 2: Run the App
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

## 📂 Project Structure
```
STDAST/
├── utils/
│   ├── APIs.py             # API key management and Gemini integration
│   ├── DOCs.py             # Document processing (PDF, DOCX, etc.)
│   ├── Theme.py            # UI theme configuration
│   └── __init__.py
├── tabs/
│   ├── Chat.py             # Chat interface
│   ├── Summ.py             # Summarization tab
│   ├── Exp.py              # Explanation tab
│   ├── KeyW.py             # Keywords tab
│   ├── Sim.py              # Similar content tab
│   ├── Links.py            # Web links tab
│   ├── QA.py               # Q&A tab
│   ├── Img.py              # Image search tab
│   ├── TimTab.py           # Timetable generator
│   └── __init__.py
├── SmartStudyAssistant.py  # Main application file
├── requirements.txt        # Python dependencies
├── packages.txt            # System dependencies
├── .gitignore              # Git ignore rules
├── README.md               # This file
└── LICENSE                 # License file
```

## 🎨 Features in Detail

### Document Support
- PDF (with OCR for scanned documents)
- Word (.docx, .doc)
- PowerPoint (.pptx)
- Excel (.xlsx)
- Text files (.txt)
- Images (.jpg, .jpeg, .png) - with OCR

### AI Capabilities
- Context-aware responses
- Multi-level explanations
- Automatic keyword extraction
- Web search integration
- Timetable optimization

## 🔐 Security

- Supports multiple API keys with automatic rotation
- No data stored on servers

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Google Gemini AI](https://ai.google.dev/)
- OCR by [Tesseract](https://github.com/tesseract-ocr/tesseract)


---

Made with ❤️ for students worldwide
