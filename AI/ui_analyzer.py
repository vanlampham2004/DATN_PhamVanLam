from AI.ollama_client import call_ollama

def analyze_ui(errors, ui_text):
    prompt = f"""
You are a UI Testing Expert.

Detected {errors} UI differences.

UI Text:
{ui_text}

Describe:
- What UI issues may exist
- Possible layout problems
- Missing or incorrect elements

Keep it short.
"""
    return call_ollama(prompt)