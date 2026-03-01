# 🤖 Swarm-OS

**No-Code Visual Operating System for Autonomous Multi-Agent AI Workflows**

Built for AMD Slingshot Hackathon 🚀

---

## 🎯 Problem Statement

In today's AI landscape, complex tasks often require multiple specialized AI agents working together. However, orchestrating these agents typically demands:

- Extensive coding knowledge
- Complex infrastructure setup
- Manual coordination between agents
- Technical expertise in async programming

This creates a barrier for non-technical users who want to leverage the power of multi-agent AI systems.

## 💡 Solution Overview

Swarm-OS is a lightweight, visual operating system that democratizes access to multi-agent AI workflows. It provides:

- **Zero-Code Interface**: Simple web dashboard - just enter your goal and click run
- **Autonomous Orchestration**: Three specialized AI agents work together automatically
- **Real-Time Visibility**: Watch agents collaborate through live logs and visual graphs
- **Production-Ready**: Built with modern async architecture for reliability and performance

### How It Works

```
User Goal → Researcher Agent → Analyst Agent → Writer Agent → Final Report
```

1. **User** enters a goal in plain English
2. **Researcher** gathers comprehensive information about the topic
3. **Analyst** analyzes findings and extracts insights
4. **Writer** creates a polished, publication-ready report

All happening automatically, with full visibility into the process.

---

## ✨ Features

### Core Capabilities
- ✅ **No-Code Operation**: Simple text input interface
- ✅ **Multi-Agent Orchestration**: Three specialized agents (Researcher, Analyst, Writer)
- ✅ **Real-Time Execution Logs**: Terminal-style display with timestamps
- ✅ **Interactive Network Graph**: Visual representation of agent workflow using pyvis
- ✅ **Async Architecture**: Efficient task handling with Python asyncio
- ✅ **Stop Control**: Ability to halt execution at any time
- ✅ **Performance Metrics**: Execution time tracking and statistics

### Technical Features
- ✅ Clean modular architecture
- ✅ Error handling and graceful degradation
- ✅ Environment-based configuration
- ✅ OpenAI GPT-3.5-turbo integration
- ✅ Responsive Streamlit UI
- ✅ Production-ready code quality

---

## 🏗️ Architecture

### System Design

```
┌─────────────────────────────────────────────────────────┐
│                    Streamlit Frontend                    │
│                      (app.py)                           │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │   Goal Input │  │  Control     │  │  Execution   │ │
│  │   Interface  │  │  Buttons     │  │  Logs        │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │         Network Graph Visualization              │  │
│  │              (pyvis + networkx)                  │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Swarm Orchestration Engine                  │
│                  (swarm_core.py)                        │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────┐      ┌──────────────┐                │
│  │ Orchestrator │─────▶│ Agent Class  │                │
│  │   - Workflow │      │  - Execute   │                │
│  │   - Graph    │      │  - Track     │                │
│  └──────────────┘      └──────────────┘                │
│                                                          │
│         ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│         │Researcher│─▶│ Analyst  │─▶│  Writer  │      │
│         └──────────┘  └──────────┘  └──────────┘      │
│                                                          │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                  OpenAI API (GPT-3.5)                   │
└─────────────────────────────────────────────────────────┘
```

### Agent Roles

1. **Researcher Agent**
   - Gathers comprehensive information
   - Identifies key facts and trends
   - Structures findings clearly

2. **Analyst Agent**
   - Analyzes research output
   - Identifies patterns and insights
   - Draws meaningful conclusions

3. **Writer Agent**
   - Creates polished final report
   - Structures content professionally
   - Ensures readability and clarity

### Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Backend**: Python 3.10+ with asyncio
- **Visualization**: pyvis + networkx
- **AI Engine**: OpenAI GPT-3.5-turbo
- **Architecture**: Async multi-agent orchestration

---

## 🚀 How to Run

### Prerequisites

- Python 3.10 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- pip package manager

### Installation Steps

1. **Navigate to project directory**
```bash
cd swarm-os
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.env` file in the project root:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

Or copy from the example:
```bash
cp .env.example .env
# Then edit .env and add your API key
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open in browser**

The application will automatically open at `http://localhost:8501`

---

## 📖 Usage Guide

### Basic Workflow

1. **Enter Your Goal**
   - Type your objective in the text area
   - Example: "Research the latest trends in quantum computing and create a comprehensive report"

2. **Run the Swarm**
   - Click the "🚀 Run Swarm" button
   - Watch the agents work in real-time

3. **Monitor Progress**
   - View live execution logs in the terminal panel
   - See the network graph showing agent interactions
   - Track execution time and status

4. **Review Results**
   - Check individual agent outputs in separate tabs
   - Read the final polished report
   - View execution summary and metrics

5. **Stop if Needed**
   - Click "🛑 Stop" button to halt execution at any time

### Example Use Cases

- **Research & Analysis**: "Analyze the impact of AI on healthcare"
- **Market Research**: "Research competitors in the electric vehicle market"
- **Content Creation**: "Create a comprehensive guide on sustainable living"
- **Technical Documentation**: "Explain blockchain technology for beginners"
- **Trend Analysis**: "Identify emerging trends in renewable energy"

---

## 📁 Project Structure

```
swarm-os/
├── app.py              # Main Streamlit application (Frontend)
├── swarm_core.py       # Multi-agent orchestration engine (Backend)
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── README.md          # This file
```

### File Descriptions

- **app.py**: Streamlit UI with goal input, control buttons, logs, graph visualization, and results display
- **swarm_core.py**: Agent class, orchestrator logic, workflow execution, and graph generation
- **requirements.txt**: All required Python packages
- **.env.example**: Template for environment configuration

---

## 🔧 Technical Details

### Async Architecture

Swarm-OS uses Python's `asyncio` for efficient concurrent execution:

```python
async def run_workflow(goal, log_callback, stop_check):
    # Sequential agent execution with async I/O
    for agent in agents:
        output = await agent.execute(task, context)
        context = output  # Pass to next agent
```

### Agent Communication

Agents communicate through context passing:
- Each agent receives the previous agent's output as context
- Sequential processing ensures coherent workflow
- Context accumulation enables sophisticated reasoning

### Error Handling

- Graceful degradation on API failures
- User-friendly error messages
- Execution state preservation
- Stop functionality for user control

---

## 🎨 UI Components

### Dashboard Layout

- **Left Panel**: Goal input, control buttons, network graph
- **Right Panel**: Real-time execution logs
- **Bottom Section**: Tabbed results display

### Visual Elements

- Terminal-style logs with green text on dark background
- Interactive network graph with colored nodes
- Loading spinners and status indicators
- Clean, professional styling

---

## 🔐 Security & Best Practices

- ✅ API keys stored in environment variables (never in code)
- ✅ `.env` file excluded from version control
- ✅ Input validation and sanitization
- ✅ Error handling for API failures
- ✅ Secure async execution

### Important Notes

- Never commit your `.env` file with real API keys
- Keep your OpenAI API key secure
- Monitor API usage to control costs
- Use environment variables for all sensitive data

---

## 🚧 Future Enhancements

Potential features for future versions:

- [ ] Custom agent creation interface
- [ ] Parallel agent execution mode
- [ ] Agent memory and context persistence
- [ ] Export reports to PDF/Markdown
- [ ] Integration with more LLM providers (Anthropic, Cohere)
- [ ] Agent performance analytics dashboard
- [ ] Workflow templates library
- [ ] Multi-user support with authentication
- [ ] Agent marketplace for specialized roles
- [ ] Real-time collaboration features

---

## 🏆 Built for AMD Slingshot Hackathon

Swarm-OS demonstrates the power of multi-agent AI systems in a simple, accessible package. It showcases:

- **Innovation**: Novel approach to no-code AI orchestration
- **Usability**: Intuitive interface for non-technical users
- **Technical Excellence**: Clean architecture with modern async patterns
- **Practical Value**: Solves real problems in research and content creation

---

## 📄 License

MIT License - Feel free to use, modify, and distribute for your projects.

---

## 🤝 Contributing

Contributions are welcome! This is an MVP designed for simplicity and extensibility.

### How to Contribute

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review code comments for implementation details

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [OpenAI](https://openai.com/)
- Visualization by [pyvis](https://pyvis.readthedocs.io/)
- Network analysis with [NetworkX](https://networkx.org/)

---

**Built with ❤️ for AMD Slingshot Hackathon**

*Swarm-OS v1.0 - Making Multi-Agent AI Accessible to Everyone*
