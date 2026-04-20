import time

from utils.logger import setup_logger
from utils.evaluator import evaluate_ui
from utils.report_html import generate_html_report

from tests.test_ui_login import capture_login_ui
from vision.compare_advanced import compare_and_highlight
from vision.ocr import extract_text
from generator.test_case_gen import generate_test_cases
from utils.excel_writer import save_to_excel
from AI.ui_analyzer import analyze_ui

logger = setup_logger()

try:
    logger.info("START UI TEST PIPELINE")

    timestamp = time.strftime("%Y%m%d_%H%M%S")

    # 1. Capture
    screenshot = capture_login_ui()
    logger.info(f"Screenshot: {screenshot}")

    # 2. Compare
    diff_path = f"reports/diff_{timestamp}.png"
    errors, diff = compare_and_highlight(
        "baseline/login.png",
        screenshot,
        diff_path
    )

    logger.info(f"Errors: {errors}")

    # 3. Evaluate
    result = evaluate_ui(errors)
    logger.info(f"Result: {result}")

    # 4. OCR
    text = extract_text(screenshot)

    # 5. AI test case
    cases = generate_test_cases(text)

    excel_path = f"reports/login_{timestamp}.xlsx"
    save_to_excel(cases, excel_path)

    # 6. AI analyze UI
    analysis = analyze_ui(errors, text)

    # 7. HTML report
    report_path = generate_html_report(
        result,
        errors,
        screenshot,
        diff,
        analysis
    )

    logger.info(f"Report: {report_path}")
    logger.info("DONE")

except Exception as e:
    logger.error("ERROR", exc_info=True)