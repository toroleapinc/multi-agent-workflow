"""Track agent execution for debugging."""
import json
import time
from dataclasses import dataclass, asdict
from typing import List

@dataclass
class AgentTrace:
    agent_name: str
    start_time: float
    end_time: float
    input_summary: str
    output_summary: str
    success: bool

class ExecutionTracker:
    def __init__(self):
        self.traces: List[AgentTrace] = []

    def record(self, trace: AgentTrace):
        self.traces.append(trace)

    def summary(self):
        total = sum(t.end_time - t.start_time for t in self.traces)
        return {
            'total_agents': len(self.traces),
            'total_time_s': total,
            'agents': [asdict(t) for t in self.traces],
        }

    def save(self, path='trace.json'):
        with open(path, 'w') as f:
            json.dump(self.summary(), f, indent=2)
