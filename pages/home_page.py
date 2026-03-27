from pages.base_page import BasePage
from utils.image_compare import compare_images
import cv2

class HomePage(BasePage):

    BASELINE = "baseline/home.png"
    CURRENT = "screenshots/home.png"

    def check_ui(self):
        self.screenshot(self.CURRENT)

        score, diff = compare_images(self.BASELINE, self.CURRENT)

        cv2.imwrite("diff/home_diff.png", diff)

        return score