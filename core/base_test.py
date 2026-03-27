from core.driver_manager import DriverManager

class BaseTest:

    def setup_method(self):
        self.driver_manager = DriverManager()
        self.driver = self.driver_manager.start()

    def teardown_method(self):
        self.driver_manager.quit()