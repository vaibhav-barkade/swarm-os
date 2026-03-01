"""
Swarm-OS Core: Multi-Agent Orchestration Engine
Handles agent creation, task execution, and workflow coordination
"""

import asyncio
from typing import Dict, Callable, Optional
from openai import AsyncOpenAI
import os
import time
from pyvis.network import Network


class Agent:
    """Individual AI agent with specific role and capabilities"""
    
    def __init__(self, name: str, role: str, system_prompt: str, color: str = "#667eea"):
        self.name = name
        self.role = role
        self.system_prompt = system_prompt
        self.color = color
        self.output = ""
        self.execution_time = 0
    
    async def execute(
        self, 
        task: str, 
        context: str = "", 
        log_callback: Optional[Callable] = None,
        stop_check: Optional[Callable] = None
    ) -> str:
        """Execute agent task using OpenAI API"""
        start_time = time.time()
        
        try:
            # Check if stop requested
            if stop_check and stop_check():
                if log_callback:
                    log_callback(f"⚠️ {self.name} stopped by user")
                return "Execution stopped by user"
            
            if log_callback:
                log_callback(f"🤖 {self.name} starting task...")
            
            client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"Task: {task}\n\nContext from previous agent: {context}"}
            ]
            
            if log_callback:
                log_callback(f"📡 {self.name} sending request to OpenAI...")
            
            response = await client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=600
            )
            
            self.output = response.choices[0].message.content
            self.execution_time = time.time() - start_time
            
            if log_callback:
                log_callback(f"✅ {self.name} completed in {self.execution_time:.2f}s")
                preview = self.output[:100].replace('\n', ' ')
                log_callback(f"📄 Preview: {preview}...")
            
            return self.output
            
        except Exception as e:
            self.execution_time = time.time() - start_time
            error_msg = f"❌ {self.name} error: {str(e)}"
            if log_callback:
                log_callback(error_msg)
            return f"Error in {self.name}: {str(e)}"


class SwarmOrchestrator:
    """Orchestrates multi-agent workflows"""
    
    def __init__(self):
        self.agents = self._create_default_agents()
    
    def _create_default_agents(self):
        """Create the default 3-agent swarm: Researcher, Analyst, Writer"""
        
        researcher = Agent(
            name="Researcher",
            role="Research Specialist",
            system_prompt="""You are an expert research specialist. Your job is to:
1. Gather comprehensive information about the given topic
2. Identify key facts, trends, and insights
3. Organize findings in a clear, structured format
4. Provide bullet points with the most important discoveries

Be thorough but concise. Focus on accuracy and relevance.""",
            color="#FF6B6B"
        )
        
        analyst = Agent(
            name="Analyst",
            role="Data Analyst",
            system_prompt="""You are a skilled data analyst. Your job is to:
1. Analyze the research findings provided to you
2. Identify patterns, trends, and correlations
3. Draw meaningful insights and conclusions
4. Highlight the most significant findings
5. Provide analytical perspective

Be analytical and objective. Focus on extracting actionable insights.""",
            color="#4ECDC4"
        )
        
        writer = Agent(
            name="Writer",
            role="Content Writer",
            system_prompt="""You are a professional content writer. Your job is to:
1. Take the analysis provided and create a polished final report
2. Structure the content with clear sections
3. Write in a clear, engaging, and professional tone
4. Include an executive summary
5. Make it readable and well-formatted

Create a comprehensive, publication-ready report.""",
            color="#95E1D3"
        )
        
        return [researcher, analyst, writer]
    
    def generate_graph_html(self) -> str:
        """Generate interactive network graph visualization using pyvis"""
        net = Network(
            height="380px",
            width="100%",
            bgcolor="#ffffff",
            font_color="#333333",
            directed=True
        )
        
        # Configure physics
        net.set_options("""
        {
            "physics": {
                "enabled": true,
                "stabilization": {
                    "enabled": true,
                    "iterations": 100
                }
            },
            "nodes": {
                "font": {
                    "size": 16,
                    "face": "arial"
                }
            },
            "edges": {
                "arrows": {
                    "to": {
                        "enabled": true,
                        "scaleFactor": 0.5
                    }
                },
                "smooth": {
                    "type": "cubicBezier"
                }
            }
        }
        """)
        
        # Add nodes for each agent
        for i, agent in enumerate(self.agents):
            net.add_node(
                i,
                label=f"{agent.name}\n({agent.role})",
                color=agent.color,
                size=30,
                title=f"{agent.name}: {agent.role}"
            )
        
        # Add edges (sequential flow)
        for i in range(len(self.agents) - 1):
            net.add_edge(i, i + 1, width=2)
        
        # Generate HTML
        return net.generate_html()
    
    async def run_workflow(
        self, 
        goal: str, 
        log_callback: Optional[Callable] = None,
        stop_check: Optional[Callable] = None
    ) -> Dict[str, str]:
        """Execute sequential agent workflow"""
        results = {}
        
        if log_callback:
            log_callback("🚀 Swarm-OS workflow initiated")
            log_callback(f"📋 Goal: {goal}")
            log_callback("=" * 60)
        
        context = goal
        
        for i, agent in enumerate(self.agents, 1):
            # Check if stop requested
            if stop_check and stop_check():
                if log_callback:
                    log_callback("⚠️ Workflow stopped by user")
                break
            
            if log_callback:
                log_callback(f"\n[Agent {i}/{len(self.agents)}] Executing {agent.name}...")
            
            output = await agent.execute(context, context, log_callback, stop_check)
            results[agent.name] = output
            context = output  # Pass output to next agent
        
        if log_callback:
            log_callback("\n" + "=" * 60)
            if stop_check and stop_check():
                log_callback("⚠️ Workflow stopped")
            else:
                log_callback("✨ Workflow completed successfully!")
        
        return results
