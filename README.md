# LangGraph Chatbot Application

A full-stack chatbot application built with **LangGraph**, **LangChain**, and **Streamlit**, leveraging the Mistral AI language model for intelligent conversational responses.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Frontend Variants](#frontend-variants)
- [Technical Stack](#technical-stack)

---

## 🎯 Overview

This project demonstrates a modern chatbot implementation using LangGraph's state management capabilities combined with Streamlit's interactive UI framework. The application supports multiple conversation threads, real-time message streaming, and persistent conversation history.

---

## ✨ Features

- **Multi-threaded Conversations**: Manage multiple independent chat sessions with unique thread IDs
- **Real-time Streaming**: Stream AI responses token-by-token for a responsive user experience
- **Conversation Persistence**: Store and retrieve conversation history with LangGraph checkpointer
- **Stateful Message Management**: Advanced message handling with automatic message aggregation
- **Interactive UI**: Clean Streamlit interface with sidebar navigation
- **Mistral AI Integration**: Powered by Mistral Small 2506 language model
- **Multiple Frontend Implementations**: Choose from basic chat, threaded conversations, or streaming variants

---

## 🏗️ Architecture

The application follows a modular architecture separating backend logic from frontend presentation:

```
┌──────────────────────────────────┐
│    Streamlit Frontend Layer      │
│  (Multiple UI Implementations)   │
└──────────────┬───────────────────┘
               │
┌──────────────▼───────────────────┐
│   LangGraph Backend Layer        │
│  (State Management & Workflow)   │
└──────────────┬───────────────────┘
               │
┌──────────────▼───────────────────┐
│  LangChain / Mistral AI Layer    │
│  (Language Model Integration)    │
└──────────────────────────────────┘
```

---

## 📁 Project Structure

```
langgraph_backend.py                  # Core backend logic with LangGraph workflow
streamlit_frontend.py                 # Basic chat interface
streamlit_frontend_chat.py            # Multi-threaded chat with conversation history
streamlit_frontend_streaming.py       # Chat with real-time streaming responses
streamlit_frontend_threading.py       # Advanced threading with concurrent streaming
requirements.txt                      # Python dependencies
README.md                             # This file
```

---

## 📋 Prerequisites

- **Python**: 3.8 or higher
- **pip**: Python package manager
- **Mistral API Key**: Required for LLM access (set in `.env` file)

---

## 🚀 Installation

### 1. Clone or Download the Project

```bash
cd path/to/LangGraph_Projects
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

---

## 💻 Usage

### Running the Backend

The `langgraph_backend.py` module exports a `chatbot` object that handles all conversation logic. It's imported and used by the frontend implementations.

### Running the Frontend Variants

Choose one of the following Streamlit applications:

#### **Option 1: Basic Chat Interface**
```bash
streamlit run streamlit_frontend.py
```
- Simple single-thread chat interface
- Best for: Quick prototyping and basic testing

#### **Option 2: Multi-threaded Chat with Conversation History**
```bash
streamlit run streamlit_frontend_chat.py
```
- Multiple independent conversations
- Sidebar with conversation navigation
- Auto-generated chat titles from first message
- Best for: Full-featured chatbot experience

#### **Option 3: Streaming Chat Interface**
```bash
streamlit run streamlit_frontend_streaming.py
```
- Real-time token streaming
- Single conversation thread
- Best for: Observing token-by-token response generation

#### **Option 4: Advanced Threading with Concurrent Streaming**
```bash
streamlit run streamlit_frontend_threading.py
```
- Multi-threaded conversations with streaming
- Concurrent message processing
- Best for: Production-ready implementation

---

## ⚙️ Configuration

### Backend Configuration

Edit `langgraph_backend.py` to customize:

- **LLM Model**: Change `'mistral-small-2506'` to any available Mistral model
- **Checkpointer**: Replace `InMemorySaver()` with `SqliteSaver()` for persistent storage
- **State Management**: Extend `ChatState` TypedDict for additional conversation metadata

### Frontend Configuration

Customize Streamlit behavior in `streamlit_frontend_chat.py` and other frontends:

- **Chat Title Length**: Modify the truncation limit in `generate_chat_title()`
- **Thread Display**: Adjust the sidebar conversation list ordering
- **UI Components**: Customize colors, fonts, and layouts using Streamlit configuration

---

## 🎮 Frontend Variants Comparison

| Feature | Basic | Chat | Streaming | Threading |
|---------|-------|------|-----------|-----------|
| Multiple Threads | ❌ | ✅ | ❌ | ✅ |
| Real-time Streaming | ❌ | ❌ | ✅ | ✅ |
| Conversation History | ❌ | ✅ | ❌ | ✅ |
| Sidebar Navigation | ❌ | ✅ | ❌ | ✅ |
| Persistent Storage | ❌ | ✅ | ❌ | ✅ |

---

## 🛠️ Technical Stack

### Core Frameworks
- **LangGraph**: `0.6.1` - State graph management and workflow orchestration
- **LangChain**: `0.3.27` - LLM integration and utilities
- **Streamlit**: `^1.0` - Interactive web UI framework

### Language Model
- **Mistral AI**: via `langchain-mistralai` - Language model provider

### Data & Storage
- **SQLite**: via `langgraph-checkpoint-sqlite` - Persistent conversation storage
- **Pydantic**: `2.11.7` - Data validation and serialization
- **Pandas**: `2.3.1` - Data manipulation (optional utilities)

### Additional Libraries
- **httpx**: `0.28.1` - Async HTTP client
- **python-dotenv**: `0.9.9` - Environment variable management

---

## 🔄 Message Flow

```
User Input
    ↓
Streamlit UI (Input Component)
    ↓
HumanMessage Creation
    ↓
LangGraph Invoke/Stream
    ↓
Mistral AI LLM Processing
    ↓
AIMessage Response
    ↓
Message History Update
    ↓
Streamlit Chat Display
```

---

## 📝 Example Conversation

```
User: "What is LangGraph?"
Assistant: "LangGraph is a framework built on top of LangChain for orchestrating complex 
multi-agent workflows. It provides a graph-based approach to state management..."

[Conversation history persisted and available for recall]
```

---

## 🐛 Troubleshooting

### Issue: `ModuleNotFoundError`
**Solution**: Ensure all dependencies are installed with `pip install -r requirements.txt`

### Issue: `MISTRAL_API_KEY not found`
**Solution**: Create a `.env` file with your Mistral API key

### Issue: Streamlit port already in use
**Solution**: 
```bash
streamlit run streamlit_frontend.py --server.port 8501
```

### Issue: Messages not persisting
**Solution**: Use `SqliteSaver()` instead of `InMemorySaver()` in `langgraph_backend.py`

---

## 📚 Resources

- [LangGraph Documentation](https://docs.langchain.com/langgraph/)
- [LangChain Documentation](https://docs.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Mistral AI Documentation](https://docs.mistral.ai/)

---

## 📄 License

This project is provided as-is for educational and development purposes.

---

## ✍️ Notes

- The in-memory checkpointer stores conversation state only during the current session
- For production use, consider migrating to SQLite-based persistence
- Thread IDs are generated using UUID4 for unique identification across sessions
- Message streaming is optimized for real-time user feedback

---

**Version**: 1.0  
**Last Updated**: June 2026  
**Status**: Active Development

**More Files Will be uploaded as Learning Proceeds**