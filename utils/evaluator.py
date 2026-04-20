def evaluate_ui(errors, threshold=5):
    if errors <= threshold:
        return "PASS"
    return "FAIL"