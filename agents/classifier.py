"""Classifier agent: categorizes tasks."""
import openai
from .base import BaseAgent

CATEGORIES = ['financial_analysis', 'market_research', 'data_extraction', 'summarization', 'comparison', 'general']

class ClassifierAgent(BaseAgent):
    name = "classifier"
    
    def __init__(self, model='gpt-3.5-turbo'):
        self.model = model
        self.client = openai.OpenAI()
    
    def process(self, input_data, context=None):
        parsed = context.get('parser', {}) if context else {}
        intent = parsed.get('intent', str(input_data))
        
        prompt = f"Classify this intent into one of: {', '.join(CATEGORIES)}\n\nIntent: {intent}\n\nCategory:"
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0, max_tokens=20,
        )
        category = response.choices[0].message.content.strip().lower()
        if category not in CATEGORIES:
            category = 'general'
        return {"category": category}
