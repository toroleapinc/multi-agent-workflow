"""Analyzer agent: performs analysis based on task type."""
import openai
from .base import BaseAgent

class AnalyzerAgent(BaseAgent):
    name = "analyzer"
    
    def __init__(self, model='gpt-4'):
        self.model = model
        self.client = openai.OpenAI()
    
    def process(self, input_data, context=None):
        parsed = context.get('parser', {}) if context else {}
        category = context.get('classifier', {}).get('category', 'general') if context else 'general'
        
        system_prompts = {
            'financial_analysis': "You are a financial analyst. Provide detailed quantitative analysis.",
            'market_research': "You are a market researcher. Analyze market trends and competition.",
            'summarization': "You are a summarization expert. Be concise and capture key points.",
        }
        system = system_prompts.get(category, "You are a helpful analyst.")
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": f"Task: {input_data}\n\nParsed info: {parsed}"},
            ],
            temperature=0.2,
        )
        return {"analysis": response.choices[0].message.content}
