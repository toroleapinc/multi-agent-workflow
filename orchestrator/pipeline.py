"""Sequential pipeline orchestrator."""
import logging
from typing import List
from agents.base import BaseAgent, AgentResult

logger = logging.getLogger(__name__)

class Pipeline:
    def __init__(self, agents: List[BaseAgent]):
        self.agents = agents

    def run(self, input_data):
        """Run agents in sequence, passing context between them."""
        context = {}
        results = []
        
        for agent in self.agents:
            logger.info(f"Running {agent.name}...")
            result = agent.run(input_data, context)
            context[agent.name] = result.output
            results.append(result)
            logger.info(f"  {agent.name} completed in {result.duration_ms:.0f}ms")
        
        return PipelineResult(results=results, final_output=results[-1].output if results else None)

class PipelineResult:
    def __init__(self, results, final_output):
        self.results = results
        self.output = final_output
        self.total_duration = sum(r.duration_ms for r in results)
    
    def __repr__(self):
        return f"PipelineResult(agents={len(self.results)}, duration={self.total_duration:.0f}ms)"
