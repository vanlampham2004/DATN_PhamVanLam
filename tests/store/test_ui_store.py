import time

from selenium import webdriver

from vision.screenshot import take_fullpage_screenshot


def capture_store_ui():
    driver = None
    screenshots = []

    devices = {
        "desktop": (1920, 1080),
        "tablet": (768, 1024),
        "mobile": (390, 844)
    }

    try:
        driver = webdriver.Chrome()

        for device, (width, height) in devices.items():
            driver.set_window_size(width, height)

            driver.get("https://torano.vn/pages/he-thong-cua-hang")

            time.sleep(3)

            parts = take_fullpage_screenshot(
                driver,
                feature=f"store_{device}"
            )

            screenshots.extend(parts)

        return screenshots

    except Exception as e:
        print(f"Capture store error: {e}")
        return None

    finally:
        if driver:
            driver.quit()