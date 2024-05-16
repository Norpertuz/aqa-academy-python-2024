from selenium.webdriver.common.by import By


class LoginPage:
    # URL of the page
    URL = "https://github.com/login"
    # Error message we should obtain
    ERROR_MESSAGE = "Incorrect username or password."

    def __init__(self, app) -> None:
        self.app = app

    # user methods
    def try_login(self, username: str, password: str):
        self.app.browser.find_element(By.ID, "login_field").send_keys(username)
        self.app.browser.find_element(By.ID, "password").send_keys(password)
        self.app.browser.find_element("name", "commit").click()

    def navigate_to(self):
        self.app.navigate_to(self.URL)

    # check functions
    def check_wrong_creds_message(self) -> bool:
        error_text = self.app.browser.find_element(By.CLASS_NAME, "js-flash-alert").text
        return error_text.strip() == self.ERROR_MESSAGE
