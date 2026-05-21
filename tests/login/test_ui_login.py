import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from vision.screenshot import take_fullpage_screenshot


def capture_login_ui():
    driver = None
    screenshots = []

    devices = {
        "desktop": (1920, 1080),
        "tablet": (768, 1024),
        "mobile": (390, 844)
    }

    try:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        for device, (width, height) in devices.items():
            driver.set_window_size(width, height)
            driver.get("https://torano.vn/account/login")

            time.sleep(2)

            parts = take_fullpage_screenshot(
                driver,
                feature=f"login_{device}"
            )

            screenshots.extend(parts)

        #print("DEBUG screenshots:", screenshots)

        return screenshots

    except Exception as e:
        print(f"Capture login error: {e}")
        return None

    finally:
        if driver:
            driver.quit()