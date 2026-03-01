"""
Swarm-OS: No-Code Visual Operating System for Autonomous Multi-Agent AI Workflows
Main Streamlit Application
"""

import streamlit as st
import streamlit.components.v1 as components
import asyncio
from swarm_core import SwarmOrchestrator
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Swarm-OS Dashboard",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .terminal-box {
        background-color: #1e1e1e;
        color: #00ff00;
        padding: 20px;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
        height: 400px;
        overflow-y: auto;
        white-space: pre-wrap;
        font-size: 13px;
    }
    .output-box {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 5px;
        border-left: 4px solid #667eea;
    }
    .stButton>button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'results' not in st.session_state:
    st.session_state.results = {}
if 'running' not in st.session_state:
    st.session_state.running = False
if 'stop_requested' not in st.session_state:
    st.session_state.stop_requested = False
if 'execution_time' not in st.session_state:
    st.session_state.execution_time = 0
if 'graph_html' not in st.session_state:
    st.session_state.graph_html = None


def add_log(message: str):
    """Add timestamped message to execution logs"""
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.logs.append(f"[{timestamp}] {message}")


async def run_swarm_async(goal: str):
    """Run swarm workflow asynchronously"""
    st.session_state.logs = []
    st.session_state.running = True
    st.session_state.stop_requested = False
    st.session_state.results = {}
    
    start_time = time.time()
    
    try:
        orchestrator = SwarmOrchestrator()
        
        # Generate and save graph visualization
        graph_html = orchestrator.generate_graph_html()
        st.session_state.graph_html = graph_html
        
        # Run workflow
        results = await orchestrator.run_workflow(
            goal, 
            log_callback=add_log,
            stop_check=lambda: st.session_state.stop_requested
        )
        
        end_time = time.time()
        st.session_state.execution_time = end_time - start_time
        st.session_state.results = results
        
    except Exception as e:
        add_log(f"❌ Error: {str(e)}")
        st.session_state.results = {"error": str(e)}
    
    finally:
        st.session_state.running = False


def main():
    # Header
    st.title("🤖 Swarm-OS Dashboard")
    st.markdown("**No-Code Visual Operating System for Autonomous Multi-Agent AI Workflows**")
    st.markdown("---")
    
    # Check API key
    if not os.getenv("OPENAI_API_KEY"):
        st.error("⚠️ OpenAI API key not found!")
        st.info("Please create a `.env` file with: `OPENAI_API_KEY=your_key_here`")
        st.stop()
    
    # Main layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Goal input section
        st.markdown("### 🎯 Enter Your Goal")
        goal = st.text_area(
            "What would you like the AI swarm to accomplish?",
            placeholder="Example: Research the latest trends in quantum computing and create a comprehensive report",
            height=120,
            key="goal_input"
        )
        
        # Control buttons
        button_col1, button_col2 = st.columns(2)
        
        with button_col1:
            run_button = st.button(
                "🚀 Run Swarm", 
                type="primary", 
                disabled=st.session_state.running or not goal
            )
        
        with button_col2:
            stop_button = st.button(
                "🛑 Stop", 
                type="secondary",
                disabled=not st.session_state.running
            )
        
        if stop_button:
            st.session_state.stop_requested = True
            add_log("⚠️ Stop requested by user")
        
        if run_button and goal:
            with st.spinner("🔄 Initializing swarm..."):
                asyncio.run(run_swarm_async(goal))
                st.rerun()
        
        # Status indicator
        if st.session_state.running:
            st.info("⚙️ Swarm is running...")
        elif st.session_state.results and not st.session_state.running:
            if "error" in st.session_state.results:
                st.error("❌ Execution failed")
            else:
                st.success(f"✅ Completed in {st.session_state.execution_time:.2f}s")
        
        # Swarm graph visualization
        st.markdown("### 🕸️ Swarm Network Graph")
        if st.session_state.graph_html:
            components.html(st.session_state.graph_html, height=400, scrolling=False)
        else:
            st.info("Graph will appear when swarm starts running")
    
    with col2:
        # Execution logs
        st.markdown("### 📟 Execution Logs")
        log_content = "\n".join(st.session_state.logs) if st.session_state.logs else "Waiting for execution..."
        st.markdown(f'<div class="terminal-box">{log_content}</div>', unsafe_allow_html=True)
    
    # Results section
    if st.session_state.results and "error" not in st.session_state.results:
        st.markdown("---")
        st.markdown("## 📊 Results")
        
        tab1, tab2, tab3, tab4 = st.tabs(["🔍 Research", "📊 Analysis", "✍️ Final Report", "📈 Summary"])
        
        with tab1:
            st.markdown("### Researcher Output")
            if "Researcher" in st.session_state.results:
                st.markdown(f'<div class="output-box">{st.session_state.results["Researcher"]}</div>', 
                          unsafe_allow_html=True)
        
        with tab2:
            st.markdown("### Analyst Output")
            if "Analyst" in st.session_state.results:
                st.markdown(f'<div class="output-box">{st.session_state.results["Analyst"]}</div>', 
                          unsafe_allow_html=True)
        
        with tab3:
            st.markdown("### Writer Output")
            if "Writer" in st.session_state.results:
                st.success(st.session_state.results["Writer"])
        
        with tab4:
            st.markdown("### Execution Summary")
            st.metric("Total Execution Time", f"{st.session_state.execution_time:.2f}s")
            st.metric("Agents Executed", len([k for k in st.session_state.results.keys() if k != "error"]))
            st.metric("Status", "Success ✅")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>"
        "Built with ❤️ for AMD Slingshot Hackathon | Swarm-OS v1.0 | Powered by OpenAI"
        "</div>", 
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
