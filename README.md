# Portus Testbench

Portus Testbench is a modular CLI environment for experimenting with Gemini API models in various use cases and can be adapted for any OpenAI-compatible API models:

- 💬 Chat (Contextual Conversation)
- 🎧 Audio Understanding (e.g., MP3 analysis & transcription)
- 🖼️ Image Understanding (e.g., captioning, OCR-style inspection, text extraction, image description)
- 📄 Document Understanding (e.g., OCR, text extraction, PDF summarization)

This tool is built mainly for **testing**, and **comparing** and as a starting point for **learning** about modern LLM modalities in real-world tasks.

---

## 🛠️ Requirements

- Python 3.10+
- Pip
- Internet access (for API calls)
- API key(s) from either:
  - [Google Gemini](https://aistudio.google.com/app/apikey)
  - [OpenAI](https://platform.openai.com/account/api-keys)

---

## 📦 Installation

1. **Clone this repository**:

```bash
git clone https://github.com/yourname/portus_api_testbench.git
cd portus_api_testbench
```

2. **Create a virtual environment** (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Configure API keys**:

Rename `.env.example` to `.env` and provide your keys:

```env
OPENAI_API_KEY=your-openai-api-key
GEMINI_API_KEY=your-gemini-api-key
```

---

## 🚀 Usage

Launch the testbench with:

```bash
python main.py
```

You will be presented with a menu to select:

1. Chat  
2. Audio  
3. Image  
4. Documents

You can also run specific modes directly:

```bash
python main.py --chat
python main.py --audio
python main.py --image
python main.py --docs
```

---

## 📂 File Structure

```
portus_core/           - Engines for each mode (chat, audio, docs, image)
interface/cli/         - CLI entrypoints for each mode
portus_api_module/     - API wrappers and client management
portus_context_module/ - Context trimming, summarization, and memory logic for chat
config_manager.py      - Configuration loader
portus_manager.py      - Main interface and menu logic
.env.example           - Sample environment file
```

---

## ⚠️ Notes

- PDF and image support is limited to **inline uploads (<20MB)**.
- Gemini API has specific model limits (e.g., `gemini-2.0-flash`).
- Error messages are printed directly for transparency during learning.
- Streaming behavior is shown in token-by-token mode if supported.

---

## 🧪 Designed For

- Developers exploring LLM APIs
- Educators building interactive teaching tools
- Makers comparing OpenAI vs. Gemini capabilities
- Students learning how to work with multimodal AI
