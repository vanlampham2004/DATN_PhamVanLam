from AI.ollama_client import call_ollama
from AI.prompt_builder import build_ui_prompt


def generate_test_cases(
        image_context,
        feature_name="UI",
        n=5
):
    clean_context = image_context[:500]

    prompt = build_ui_prompt(
        clean_context,
        feature_name,
        n
    )

    result = call_ollama(
        prompt,
        timeout=90
    )

    if result and result.strip():
        return result

    return ""