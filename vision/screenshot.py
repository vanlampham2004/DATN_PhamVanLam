import os
import time
import math


def take_fullpage_screenshot(driver, feature="login"):
    folder = f"screenshots/{feature}"
    os.makedirs(folder, exist_ok=True)

    # về đầu trang
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    total_height = driver.execute_script("""
        return Math.max(
            document.body.scrollHeight,
            document.documentElement.scrollHeight
        );
    """)

    viewport_height = driver.execute_script("""
        return window.innerHeight || document.documentElement.clientHeight;
    """)

    screenshots = []

    total_parts = math.ceil(total_height / viewport_height)

    for index in range(total_parts):
        scroll_y = index * viewport_height

        # nếu là ảnh cuối thì scroll đúng xuống cuối trang
        if index == total_parts - 1:
            scroll_y = total_height - viewport_height

        driver.execute_script("""
            window.scrollTo(0, arguments[0]);
            document.documentElement.scrollTop = arguments[0];
            document.body.scrollTop = arguments[0];
        """, scroll_y)

        time.sleep(1)

        # lấy vị trí scroll thực tế để đặt tên/debug
        real_y = driver.execute_script("""
            return window.pageYOffset 
                || document.documentElement.scrollTop 
                || document.body.scrollTop 
                || 0;
        """)

        path = f"{folder}/{feature}_{index}_y{int(real_y)}.png"

        driver.save_screenshot(path)
        screenshots.append(path)

    # quay lại đầu trang
    driver.execute_script("window.scrollTo(0, 0);")

    return screenshots