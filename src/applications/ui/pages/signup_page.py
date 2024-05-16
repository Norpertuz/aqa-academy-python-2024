from selenium.webdriver.common.by import By


class SignUpPage:
    # URL of the page
    URL = "https://github.com/signup"
    # Elements of the page
    ERROR_MESSAGE = "Email is invalid or already taken"

    def __init__(self, app) -> None:
        self.app = app

    # user methods
    def try_signup(self, email: str):
        self.app.browser.find_element(By.ID, "email").send_keys(email)
        self.app.browser.find_element("css selector", ".js-continue-button").click()

    def navigate_to(self):
        self.app.navigate_to(self.URL)

    # check functions
    def check_wrong_creds_message(self) -> bool:
        error_message = self.app.browser.find_element(By.CLASS_NAME, "mb-0").text
        return error_message.strip() == self.ERROR_MESSAGE
