from selenium import webdriver

class DriverManager:

    def __init__(self):
        self.driver = None

    def start(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.set_window_size(1920, 1080)
        return self.driver

    def quit(self):
        if self.driver:
            self.driver.quit()