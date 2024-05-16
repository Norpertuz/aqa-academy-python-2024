from src.applications.ui.pages.login_page import LoginPage
from src.applications.ui.pages.signup_page import SignUpPage
from src.applications.ui.base_app import BaseApp


class GitHubUI(BaseApp):

    def __init__(self, browser) -> None:
        super().__init__(browser)
        self.login_page = LoginPage(self)
        self.signup_page = SignUpPage(self)

    def try_login(self, username: str, password: str):
        return self.login_page.try_login(username, password)

    def try_singup(self, email: str):
        return self.signup_page.try_signup(email)

    def open(self):
        self.login_page.navigate_to()

    def close(self):
        self.close_browser()
