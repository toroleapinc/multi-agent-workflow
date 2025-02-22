"""Test pipeline orchestration."""
from agents.base import BaseAgent, AgentResult
from orchestrator import Pipeline

class MockAgent(BaseAgent):
    name = "mock"
    def __init__(self, output):
        self._output = output
    def process(self, input_data, context=None):
        return self._output

def test_pipeline_basic():
    agents = [MockAgent({"step": 1}), MockAgent({"step": 2})]
    pipeline = Pipeline(agents)
    result = pipeline.run("test")
    assert len(result.results) == 2
    assert result.output == {"step": 2}

def test_pipeline_context_passing():
    class ContextAware(BaseAgent):
        name = "aware"
        def process(self, input_data, context=None):
            return {"saw_keys": list(context.keys()) if context else []}
    
    pipeline = Pipeline([MockAgent({"data": True}), ContextAware()])
    result = pipeline.run("test")
    assert "mock" in result.output["saw_keys"]
