"""Dynamic agent routing based on task type."""
from typing import Dict, List
from agents.base import BaseAgent

class Router:
    def __init__(self, routes: Dict[str, List[BaseAgent]], default: List[BaseAgent] = None):
        self.routes = routes
        self.default = default or []

    def select(self, category: str) -> List[BaseAgent]:
        return self.routes.get(category, self.default)
