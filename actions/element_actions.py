import pyautogui
import os
from datetime import datetime
from config.config import Config
from vision.opencv_engine import OpenCVEngine

class ElementActions:

    def __init__(self, driver):
        self.driver = driver
        self.cv = OpenCVEngine(Config.THRESHOLD)

    def take_screenshot(self, action_name="screen"):
        os.makedirs("screenshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{action_name}_{timestamp}.png"

        file_path = os.path.join("screenshots", file_name)

        self.driver.save_screenshot(file_path)

        print(f"Saved: {file_path}")

        return file_path

    def find_element(self, image_path, action_name="find"):
        screen = self.take_screenshot(action_name)
        return self.cv.find(screen, image_path, debug_name=action_name)

    def click_by_image(self, image_path, action_name="click"):
        # chụp màn hình
        screen_path = self.take_screenshot(action_name)

        pos = self.cv.find(screen_path, image_path)

        if pos:
            x, y = pos
            pyautogui.click(x, y)
            return True

        return False
    
    def input_by_image(self, image_path, text, action_name="input"):
        pos = self.find_element(image_path, action_name)

        if pos:
            pyautogui.click(pos)
            pyautogui.write(text, interval=0.05)
            return True
        return False