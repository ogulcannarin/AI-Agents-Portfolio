# 🤖 Multi-Agent Code Factory

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Latest-green.svg)](https://langchain-ai.github.io/langgraph/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-teal.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A collaborative multi-agent system where AI agents work together to generate, review, and iteratively improve Python code. Built with LangGraph and powered by Google's Gemini AI.

## 🎯 Overview

This project demonstrates a sophisticated multi-agent architecture where two specialized AI agents collaborate:

- **👨‍💻 Developer Agent**: Generates Python code based on user requirements
- **🧪 Tester Agent**: Reviews code, identifies bugs, and provides feedback
- **🔄 Iterative Improvement**: Automatically refines code until approval (max 3 iterations)

The system showcases real-world AI collaboration patterns, making it perfect for understanding multi-agent workflows and LangGraph implementation.

## ✨ Key Features

- **Multi-Agent Collaboration**: Coordinated workflow between developer and tester agents
- **Intelligent Code Review**: Automated bug detection and quality assurance
- **Iterative Refinement**: Self-improving code generation loop
- **Modern Web UI**: Beautiful, responsive interface with real-time feedback
- **RESTful API**: FastAPI backend for seamless integration
- **Syntax Highlighting**: Clean code display with proper formatting
- **Process Visualization**: Track iterations and agent interactions

## 🏗️ Architecture

```
User Request
    ↓
Developer Agent → Generates Code
    ↓
Tester Agent → Reviews Code
    ↓
  ┌─────┴─────┐
  │           │
APPROVED    REJECTED
  │           │
 END      ← ─ ┘
     (Back to Developer)
```

The system uses LangGraph's state management to coordinate agent interactions, ensuring smooth transitions and maintaining context throughout the review cycle.

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- Google AI API key ([Get one here](https://makersuite.google.com/app/apikey))
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ogulcannarin/multi-agent-code-factory.git
   cd multi-agent-code-factory
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

### Running the Application

1. **Start the backend server**
   ```bash
   uvicorn main:app --reload --port 8000
   ```

2. **Open the web interface**
   
   Option 1: Open `index.html` directly in your browser
   
   Option 2: Use Python's HTTP server
   ```bash
   python -m http.server 8080
   ```
   Then navigate to `http://localhost:8080`

## 📡 API Documentation

### POST /generate-code

Generate code based on task description.

**Request:**
```json
{
  "gorev": "Write a function to calculate factorial"
}
```

**Response:**
```json
{
  "kod": "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n-1)",
  "durum": "ONAY",
  "tur_sayisi": 2
}
```

### GET /

System status check.

### GET /health

Health check endpoint.

## 🎨 User Interface

The web interface features:

- **Modern Design**: Gradient backgrounds and smooth animations
- **Responsive Layout**: Works on all screen sizes
- **Real-time Feedback**: Live loading indicators
- **Code Highlighting**: Syntax-aware display
- **Error Handling**: User-friendly error messages
- **Iteration Tracking**: Visual feedback on review cycles

## 📁 Project Structure

```
multi-agent-code-factory/
├── main.py              # FastAPI backend server
├── app.py               # Multi-agent system core logic
├── index.html           # Web UI
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container configuration
├── .env                 # Environment variables (not in repo)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🔧 Technical Stack

- **Backend**: FastAPI, Uvicorn
- **AI Framework**: LangGraph, LangChain
- **AI Model**: Google Gemini 1.5 Flash
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Environment**: Python 3.9+

## 🐳 Docker Support

Build and run with Docker:

```bash
docker build -t multi-agent-code-factory .
docker run -p 8000:8000 --env-file .env multi-agent-code-factory
```

## 🎯 Use Cases

- **Code Generation**: Quickly generate Python functions and classes
- **Code Review**: Automated quality assurance
- **Learning Tool**: Understand multi-agent patterns
- **Prototyping**: Rapid code prototyping with AI assistance
- **Portfolio Project**: Showcase AI/ML capabilities

## 🛠️ Development

The system is built with extensibility in mind. Key components:

- **Agent Definitions**: Easily customizable prompts and behaviors
- **State Management**: LangGraph's typed state for reliable workflows
- **Error Handling**: Robust error recovery and user feedback
- **API Design**: RESTful endpoints for easy integration

## 📝 Example Usage

**Request:** "Create a function to check if a number is prime"

**Agent Process:**
1. Developer Agent generates initial code
2. Tester Agent reviews for edge cases
3. Developer Agent refines based on feedback
4. Final approved code returned to user

## 🤝 Contributing

Contributions are welcome! This project is part of my AI/ML portfolio, demonstrating practical applications of multi-agent systems.

## 📄 License

MIT License - feel free to use this project for learning and development.

## 👨‍💻 Author

**Ogulcan Narin**

Part of the Agentic AI Portfolio series showcasing advanced AI agent implementations.

## 🔗 Related Projects

This is part 3 of my Agentic AI Portfolio:
- Part 1: LangChain Fundamentals
- Part 2: LangGraph Workflows
- **Part 3: Multi-Agent System** (This Project)

## 📚 Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Google AI Studio](https://makersuite.google.com/)

## ⚡ Performance

- Average response time: 3-8 seconds
- Typical iterations: 1-2 cycles
- Success rate: High for Python code generation tasks

---

**Note**: This project requires a valid Google AI API key. The system is designed for educational and demonstration purposes, showcasing multi-agent collaboration patterns.
