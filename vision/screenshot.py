import time

def take_screenshot(driver, path_prefix):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    path = f"screenshots/{path_prefix}_{timestamp}.png"
    driver.save_screenshot(path)
    return path