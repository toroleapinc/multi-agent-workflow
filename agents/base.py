"""Base agent interface."""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, Optional
import time

@dataclass
class AgentResult:
    agent_name: str
    output: Any
    metadata: Dict = field(default_factory=dict)
    duration_ms: float = 0

class BaseAgent(ABC):
    name: str = "base"
    
    @abstractmethod
    def process(self, input_data: Any, context: Optional[Dict] = None) -> Dict:
        """Process input and return result."""
        pass
    
    def run(self, input_data: Any, context: Optional[Dict] = None) -> AgentResult:
        """Run agent with timing."""
        start = time.time()
        result = self.process(input_data, context or {})
        duration = (time.time() - start) * 1000
        return AgentResult(agent_name=self.name, output=result, duration_ms=duration)
