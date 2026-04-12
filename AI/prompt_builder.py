def build_prompt(ui_text):
    return f"""
You are a QA Automation Engineer.

Generate test cases for the following UI:

{ui_text}

Include:
- Positive / Negative / Edge cases
- Steps
- Expected result
- Locator suggestion (xpath/css/id)
- OpenCV validation hint

Format as table.
"""