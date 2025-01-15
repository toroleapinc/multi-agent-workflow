"""Parser agent: extracts structured info from input."""
import openai
import json
from .base import BaseAgent

class ParserAgent(BaseAgent):
    name = "parser"
    
    def __init__(self, model='gpt-4'):
        self.model = model
        self.client = openai.OpenAI()
    
    def process(self, input_data, context=None):
        prompt = f"""Extract the key entities, intent, and parameters from this request.
Return JSON with: {{"entities": [...], "intent": "...", "parameters": {{...}}}}

Request: {input_data}"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        try:
            return json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            return {"raw": response.choices[0].message.content, "entities": [], "intent": "unknown"}
