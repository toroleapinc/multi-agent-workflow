# Multi-Agent Workflow

A framework for building multi-agent AI workflows where specialized agents collaborate to solve complex tasks. Each agent handles a specific step (parsing, analysis, classification, reporting) and they're orchestrated through configurable pipelines.

## Demo

```bash
pip install -r requirements.txt
python demo.py --input "Analyze the quarterly earnings report for ACME Corp"
```

This runs a 4-agent pipeline:
1. **Parser** - extracts key information from the input
2. **Classifier** - categorizes the task type
3. **Analyzer** - performs the actual analysis
4. **Reporter** - formats the output

## Install

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
```

## Custom Workflows

```python
from agents import ParserAgent, AnalyzerAgent, ReporterAgent
from orchestrator import Pipeline

pipeline = Pipeline([
    ParserAgent(),
    AnalyzerAgent(model="gpt-4"),
    ReporterAgent(format="markdown"),
])

result = pipeline.run("Your task description here")
print(result.output)
```

## Adding Custom Agents

Extend `BaseAgent` and implement `process()`:

```python
from agents.base import BaseAgent

class MyAgent(BaseAgent):
    name = "my_agent"
    
    def process(self, input_data, context):
        # your logic
        return {"result": "..."}
```

## Configuration

Agents can run in sequence (pipeline) or parallel (fan-out/fan-in). See `examples/` for patterns.
