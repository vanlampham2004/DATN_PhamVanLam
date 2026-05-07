import time
import os

def take_fullpage_screenshot(driver, feature="register"):
    folder = f"screenshots/{feature}"
    os.makedirs(folder, exist_ok=True)

    total_height = driver.execute_script("return document.body.scrollHeight")
    viewport_height = driver.execute_script("return window.innerHeight")

    screenshots = []
    index = 0

    for i in range(0, total_height, viewport_height):
        driver.execute_script(f"window.scrollTo(0, {i})")
        time.sleep(0.5)

        path = f"{folder}/{feature}_{index}.png"
        driver.save_screenshot(path)

        screenshots.append(path)
        index += 1

    return screenshots   # ✅ QUAN TRỌNG