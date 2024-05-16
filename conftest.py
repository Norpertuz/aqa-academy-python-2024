import pytest
from src.applications.ui.github_ui import GitHubUI
from src.applications.api.github_api import GitHubAPIClient
from selenium import webdriver


def pytest_html_report_title(report):
    report.title = "AQA Academy Norbert K."


# fixtures for tests
@pytest.fixture
def git_hub_ui_app():

    driver = webdriver.Chrome()

    # 1. Prestep. Navigate to Github
    githubui_app = GitHubUI(browser=driver)
    githubui_app.open()

    # generators in python
    yield githubui_app

    # Poststep. Close the App
    githubui_app.close()


@pytest.fixture
def git_hub_api_client():
    git_hub_api_client = GitHubAPIClient()

    yield git_hub_api_client
