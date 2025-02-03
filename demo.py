"""Demo: run the multi-agent pipeline."""
import argparse
import logging
from rich.console import Console
from rich.panel import Panel
from agents import ParserAgent, ClassifierAgent, AnalyzerAgent, ReporterAgent
from orchestrator import Pipeline

console = Console()
logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Task description')
    parser.add_argument('--model', default='gpt-4')
    args = parser.parse_args()

    pipeline = Pipeline([
        ParserAgent(model=args.model),
        ClassifierAgent(),
        AnalyzerAgent(model=args.model),
        ReporterAgent(format='markdown'),
    ])

    console.print(f"[bold]Input:[/bold] {args.input}")
    console.print("[dim]Running pipeline...[/dim]")

    result = pipeline.run(args.input)

    console.print(Panel(result.output.get('report', ''), title="Report"))
    console.print(f"[dim]Total time: {result.total_duration:.0f}ms[/dim]")

if __name__ == '__main__':
    main()
