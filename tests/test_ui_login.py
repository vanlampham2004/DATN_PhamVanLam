from selenium import webdriver
from vision.screenshot import take_screenshot

def capture_login_ui():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://torano.vn/account/login")

    try:
        driver.find_element("xpath", "//a[contains(text(),'Đăng nhập')]").click()
    except:
        pass
    
    screenshot_path = take_screenshot(driver, "login")

    driver.quit()
    return screenshot_path