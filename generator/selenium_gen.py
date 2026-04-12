from AI.ollama_client import call_ollama

def generate_selenium_code(test_cases):
    prompt = f"""
Generate Selenium pytest code for:

{test_cases}
"""
    return call_ollama(prompt)