from AI.ollama_client import call_ollama
from AI.prompt_builder import build_ui_prompt


def generate_test_cases(
        image_context,
        feature_name="Register UI",
        n=5
):
    """
    Sinh test case UI từ OCR/OpenCV
    """

    # =========================
    # CLEAN OCR TEXT
    # =========================
    clean_context = image_context[:400]

    # =========================
    # BUILD PROMPT
    # =========================
    prompt = build_ui_prompt(
        clean_context,
        feature_name,
        n
    )

    # =========================
    # CALL OLLAMA
    # =========================
    result = call_ollama(
        prompt,
        timeout=90
    )

    # =========================
    # FALLBACK
    # =========================
    if result:
        return result

    return """
TC001 | Verify register UI visible | Register UI should display correctly | Register UI visible | -
TC002 | Verify form elements visible | Form elements should display correctly | Form elements visible | -
TC003 | Verify layout alignment | Layout should align correctly | Layout aligned | -
TC004 | Verify text readability | Text should be readable | Text readable | -
TC005 | Verify button visibility | Button should display correctly | Button visible | -
""" 