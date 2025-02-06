"""Example: run multiple analyzers in parallel."""
from agents import ParserAgent, AnalyzerAgent
from orchestrator import Pipeline, ParallelExecutor

# parse first, then run multiple analyzers in parallel
parser = ParserAgent()
parsed = parser.run("Compare revenue growth of Apple vs Microsoft in Q3 2024")

# run financial and market analysis in parallel
parallel = ParallelExecutor([
    AnalyzerAgent(model='gpt-4'),
    AnalyzerAgent(model='gpt-3.5-turbo'),  # cheaper model for comparison
])

results = parallel.run(parsed.output, context={'parser': parsed.output})
for r in results:
    print(f"{r.agent_name}: {r.duration_ms:.0f}ms")
    print(r.output.get('analysis', '')[:200])
    print()
