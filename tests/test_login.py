from core.base_test import BaseTest
from pages.login_page import LoginPage
from config.config import Config
from utils.wait import wait_for
from vision.visual_compare import compare_images

class TestLogin(BaseTest):

    def test_login_full(self):
        self.driver.get(Config.URL)

        login = LoginPage(self.driver)

        assert login.input_email("vanlamp18@gmail.com")
        assert login.input_password("Phamvanlam2004@")
        assert login.click_login()

        success = wait_for(lambda: login.is_login_success(), timeout=10)

        assert success, "Login thất bại"

    def test_ui_compare(self):
        self.driver.get(Config.URL)

        # chụp current UI
        current = "screenshots/current.png"
        self.driver.save_screenshot(current)

        baseline = "baseline/login_image.png"

        score = compare_images(baseline, current)

        assert score > 0.85, "UI bị thay đổi"