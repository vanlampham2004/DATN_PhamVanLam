def log_result(page, score, threshold=0.95):

    status = "PASS" if score >= threshold else "FAIL"

    with open("reports/result.txt", "a") as f:
        f.write(f"{page}: {status} (score={score})\n")

    print(f"{page}: {status} ({score})")