import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from vision.screenshot import take_fullpage_screenshot


def capture_register_ui():
    driver = None

    try:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.set_window_size(1920, 1080)

        driver.get("https://torano.vn/account/register")

        time.sleep(2)

        screenshots = take_fullpage_screenshot(
            driver,
            "register"
        )

        return screenshots

    except Exception as e:
        print(f"Capture register error: {e}")
        return None

    finally:
        if driver:
            driver.quit()