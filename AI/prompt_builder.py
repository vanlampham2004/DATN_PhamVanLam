def build_prompt(ui_text):
    return f"""
You are a UI Testing Expert.

UI Text:
{ui_text}

Generate test cases.

STRICT RULE:
- Output ONLY CSV
- EXACTLY 3 columns
- Format:
Test Case ID,Description,Expected Result
- DO NOT explain anything

"""