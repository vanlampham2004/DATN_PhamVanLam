from AI.prompt_builder import build_prompt
from AI.ollama_client import call_ollama

def generate_test_cases(ui_text):
    prompt = build_prompt(ui_text)
    return call_ollama(prompt)