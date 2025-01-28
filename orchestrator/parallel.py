"""Parallel execution for independent agents."""
import asyncio
import logging
from typing import List
from agents.base import BaseAgent

logger = logging.getLogger(__name__)

class ParallelExecutor:
    def __init__(self, agents: List[BaseAgent]):
        self.agents = agents

    async def run_async(self, input_data, context=None):
        """Run all agents in parallel."""
        context = context or {}
        
        async def run_agent(agent):
            # run in thread pool since agents may be blocking
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(None, agent.run, input_data, context)
            return result
        
        tasks = [run_agent(agent) for agent in self.agents]
        results = await asyncio.gather(*tasks)
        return results

    def run(self, input_data, context=None):
        """Synchronous wrapper."""
        return asyncio.run(self.run_async(input_data, context))
