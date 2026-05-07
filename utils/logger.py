def setup_logger():
    import logging
    import os

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("UI_TEST")

    if logger.hasHandlers():   # 👈 FIX QUAN TRỌNG
        return logger

    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler("logs/test.log", encoding="utf-8")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger