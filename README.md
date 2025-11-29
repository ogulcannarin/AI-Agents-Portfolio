# 🤖 AI Agents Portfolio

Welcome to my AI Agents Portfolio! This repository showcases practical implementations of intelligent agents using cutting-edge frameworks like **LangChain**, **LangGraph**, and **Multi-Agent Systems**.

## 📋 Table of Contents

- [Overview](#overview)
- [Projects](#projects)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This portfolio demonstrates my expertise in building intelligent, autonomous AI agents that can reason, plan, and execute tasks. Each project showcases different aspects of agentic AI systems, from simple ReAct patterns to complex multi-agent orchestrations.

## 🚀 Projects

### 1. LangChain ReAct Agent
A sophisticated agent built with LangChain's ReAct (Reasoning + Acting) pattern. This agent can:
- Reason about problems step-by-step
- Use external tools to gather information
- Make decisions based on observations
- Execute actions autonomously

**Key Features:**
- Tool integration (web search, calculations, etc.)
- Step-by-step reasoning transparency
- Error handling and recovery

### 2. LangGraph Memory Agent
An advanced agent leveraging LangGraph for stateful conversations with persistent memory. This agent:
- Maintains context across multiple interactions
- Uses graph-based workflow management
- Implements complex decision trees
- Provides consistent, context-aware responses

**Key Features:**
- Persistent memory across sessions
- Graph-based state management
- Multi-turn conversation handling
- Dynamic workflow adaptation

### 3. Multi-Agent System
A collaborative system where multiple specialized agents work together to solve complex problems. Features:
- **Orchestrator Agent**: Coordinates tasks between specialized agents
- **Research Agent**: Gathers and analyzes information
- **Planning Agent**: Creates structured plans and strategies
- **Execution Agent**: Implements solutions based on plans

**Key Features:**
- Agent-to-agent communication
- Task decomposition and delegation
- Collaborative problem-solving
- Web interface for real-time interaction

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **LangChain**: Framework for building LLM applications
- **LangGraph**: State management for agentic workflows
- **Groq API**: Fast LLM inference
- **Tavily API**: Web search capabilities
- **Flask**: Web framework for the multi-agent system
- **HTML/CSS/JavaScript**: Frontend interfaces

## 🎬 Getting Started

### Prerequisites

- Python 3.8 or higher
- API Keys:
  - [Groq API Key](https://console.groq.com/)
  - [Tavily API Key](https://tavily.com/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ogulcannarin/AI-Agents-Portfolio.git
   cd AI-Agents-Portfolio
   ```

2. **Install dependencies**
   
   Each project has its own dependencies. Navigate to the specific project folder and install:
   
   ```bash
   # For any project
   cd 1-LangChain-ReAct-Agent  # or 2-LangGraph-Memory-Agent or 3-Multi-Agent-System
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in each project directory:
   
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

4. **Run the project**
   
   ```bash
   # For Python-based agents
   python main.py
   
   # For the Multi-Agent System with web interface
   cd 3-Multi-Agent-System
   python main.py
   # Then open http://localhost:5000 in your browser
   ```

## 📁 Project Structure

```
AI-Agents-Portfolio/
│
├── 1-LangChain-ReAct-Agent/
│   ├── main.py              # Main agent implementation
│   ├── requirements.txt     # Python dependencies
│   └── README.md           # Project-specific documentation
│
├── 2-LangGraph-Memory-Agent/
│   ├── main.py              # Memory-enabled agent
│   ├── requirements.txt     # Python dependencies
│   └── README.md           # Project-specific documentation
│
├── 3-Multi-Agent-System/
│   ├── main.py              # Flask backend with multi-agent orchestration
│   ├── index.html           # Web interface
│   ├── requirements.txt     # Python dependencies
│   └── README.md           # Project-specific documentation
│
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 💡 Use Cases

- **Automated Research**: Agents that can search, analyze, and summarize information
- **Task Planning**: AI systems that break down complex tasks into actionable steps
- **Decision Making**: Intelligent agents that reason through problems
- **Collaborative AI**: Multiple agents working together on complex problems

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/ogulcannarin/AI-Agents-Portfolio/issues).

## 📝 License

This project is [MIT](LICENSE) licensed.

## 📧 Contact

**Oğulcan Narin**
- GitHub: [@ogulcannarin](https://github.com/ogulcannarin)
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)

---

⭐ If you find this repository helpful, please consider giving it a star!

**Built with ❤️ using LangChain, LangGraph, and cutting-edge AI technologies**
