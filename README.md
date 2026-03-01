# swarm-os
Swarm-OS: A No-Code Visual Operating System for Autonomous Multi-Agent AI Workflows.

## Problem
Multi-agent AI systems require advanced coding skills and infrastructure setup.
Non-technical users cannot build autonomous AI workflows.

## Solution
Swarm-OS allows users to create AI agent swarms using a simple dashboard.
It auto-generates Researcher, Analyst, and Writer agents that collaborate autonomously.

## Features
- Goal-based agent creation
- Real-time swarm visualization
- Parallel multi-agent execution
- Hardware-aware architecture
- Exportable structured outputs

## Architecture
Frontend: Streamlit  
Backend: Python Async Orchestrator  
AI Layer: LLM (Local or API)  
Data Layer: Redis / SQLite  

## Built With
- Python
- Streamlit
- Asyncio
- CrewAI / LangGraph
- OpenAI API
- HuggingFace

## Usage

```bash
pip install -r requirements.txt
streamlit run app.py
