import time


def test_negative_register(git_hub_ui_app):
    """Summary: Test negative login attemp
    Steps:
    1. Navigate to login page
    2. Enter wrong creds
    3. Click login/signin button

    Expected result
    Error saying BLA appeared
    """
    # 1. Navigate to register page
    git_hub_ui_app.signup_page.navigate_to()
    time.sleep(4)
    # 2. Enter wrong creds
    git_hub_ui_app.try_singup(email="trytrytry")

    time.sleep(1)
    # Expected result
    assert git_hub_ui_app.signup_page.check_wrong_creds_message()
