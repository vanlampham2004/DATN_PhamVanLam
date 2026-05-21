import cv2
import os
from skimage.metrics import structural_similarity as ssim


def compare_ssim_and_highlight(baseline_path, current_path, diff_path):
    baseline = cv2.imread(baseline_path)
    current = cv2.imread(current_path)

    if baseline is None:
        raise FileNotFoundError(f"Baseline not found: {baseline_path}")

    if current is None:
        raise FileNotFoundError(f"Current image not found: {current_path}")

    if baseline.shape != current.shape:
        current = cv2.resize(
            current,
            (baseline.shape[1], baseline.shape[0])
        )

    gray_base = cv2.cvtColor(baseline, cv2.COLOR_BGR2GRAY)
    gray_current = cv2.cvtColor(current, cv2.COLOR_BGR2GRAY)

    score, diff = ssim(
        gray_base,
        gray_current,
        full=True
    )

    diff = (diff * 255).astype("uint8")

    thresh = cv2.threshold(
        diff,
        0,
        255,
        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU
    )[1]

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    errors = 0

    for c in contours:
        area = cv2.contourArea(c)

        if area < 500:
            continue

        x, y, w, h = cv2.boundingRect(c)

        cv2.rectangle(
            current,
            (x, y),
            (x + w, y + h),
            (0, 0, 255),
            2
        )

        errors += 1

    os.makedirs(os.path.dirname(diff_path), exist_ok=True)
    cv2.imwrite(diff_path, current)

    return errors, diff_path, round(score * 100, 2)