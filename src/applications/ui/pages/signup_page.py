class SignUpPage:
    # URL of the page
    URL = "https://github.com/signup"
    # Elements of the page
    EMAIL_FLD = '//*[@id="email"]'
    PASSWORD_FLD = '//*[@id="password"]'
    LOGIN_FLD = '//*[@id="login_field"]'
    CONTINUE_BTN = ""
    # SIGNIN_BTN = '//*[@id="login"]/div[4]/form/div/input[13]'

    # user methods
    def try_signup(self, email: str, password: str, username: str):
        pass

    def navigate_to(self):
        pass

    # check functions
    def check_wrong_creds_message(self):
        # find error message
        # check if message is equal to "BLA" text
        return False

    def check_documentation_link(self):
        pass
