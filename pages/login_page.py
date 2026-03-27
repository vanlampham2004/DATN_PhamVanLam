from actions.element_actions import ElementActions

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ElementActions(driver)
    
    def input_email(self, email):
        return self.actions.input_by_image(
            "templates/email_input.png",
            email,
            action_name="input_email"
        )

    def input_password(self, password):
        return self.actions.input_by_image(
            "templates/password_input.png",
            password,
            action_name="input_password"
        )

    def click_login(self):
        return self.actions.click_by_image(
            "templates/login2.png",
            action_name="click_login"
        )

    def is_login_success(self):
        return self.actions.find_element(
            "templates/user_name.png",
            action_name="verify_login"
        )