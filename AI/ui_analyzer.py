from AI.ollama_client import call_ollama


def analyze_ui(errors, ui_text, feature_name="Login UI"):
    if errors == 0:
        return f"{feature_name}: Giao diện PASS, không phát hiện sai khác so với baseline."

    return f"{feature_name}: Phát hiện {errors} vùng sai khác. Cần kiểm tra ảnh diff."