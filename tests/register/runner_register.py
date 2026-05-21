import os
import shutil

from utils.logger import setup_logger
from utils.evaluator import evaluate_ui
from utils.report_html import generate_html_report
from utils.excel_writer import save_to_excel

from tests.register.test_ui_register import capture_register_ui
from vision.compare_ssim import compare_ssim_and_highlight
from vision.ocr import extract_text
from generator.test_case_gen import generate_test_cases
from AI.ui_analyzer import analyze_ui

logger = setup_logger()


def main():
    baseline_dir = "baseline/register"
    report_dir = "reports/register"

    os.makedirs(baseline_dir, exist_ok=True)
    os.makedirs(report_dir, exist_ok=True)

    logger.info("START REGISTER UI TEST PIPELINE")

    try:
        screenshots = capture_register_ui()

        if not screenshots:
            logger.error("Capture failed")
            return

        logger.info(f"Capture done: {len(screenshots)} images")

        total_errors = 0
        diff_images = []

        for shot in screenshots:
            name = os.path.basename(shot).replace(".png", "")

            baseline_path = f"{baseline_dir}/{name}.png"
            diff_path = f"{report_dir}/diff_{name}.png"

            if not os.path.exists(baseline_path):
                shutil.copy(shot, baseline_path)
                logger.info(f"Baseline created: {name}.png")

            errors, diff, ssim_score = compare_ssim_and_highlight(
                baseline_path,
                shot,
                diff_path
            )

            total_errors += errors
            diff_images.append(diff)

            logger.info(
                f"Compare {name}: {errors} differences | ssim: {ssim_score:.4f}"
            )

        result = evaluate_ui(total_errors)
        logger.info(f"Result: {result}")

        text = ""

        for shot in screenshots:
            try:
                text += extract_text(shot) + "\n"
            except Exception as e:
                logger.warning(f"OCR skipped for {shot}: {e}")

        logger.info("OCR done")

        cases = generate_test_cases(
            text,
            feature_name="Register UI",
            n=5
        )

        excel_path = f"{report_dir}/test_cases_register.xlsx"
        save_to_excel(cases, excel_path)

        logger.info(f"Excel saved: {excel_path}")

        analysis = analyze_ui(
            total_errors,
            text,
            feature_name="Register UI"
        )

        report_path = f"{report_dir}/report.html"

        generate_html_report(
            result,
            total_errors,
            screenshots,
            diff_images,
            analysis,
            report_path
        )

        logger.info(f"Report saved: {report_path}")
        logger.info("DONE REGISTER UI TEST")

    except Exception as e:
        logger.error(f"ERROR: {e}", exc_info=True)


if __name__ == "__main__":
    main()