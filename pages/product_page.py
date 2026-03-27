from pages.base_page import BasePage
from utils.image_compare import compare_images
import cv2

class ProductPage(BasePage):

    BASELINE = "baseline/product.png"
    CURRENT = "screenshots/product.png"

    def check_ui(self):
        self.screenshot(self.CURRENT)

        score, diff = compare_images(self.BASELINE, self.CURRENT)

        cv2.imwrite("diff/product_diff.png", diff)

        return score