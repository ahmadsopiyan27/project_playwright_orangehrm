import pytest
import allure
from playwright.sync_api import sync_playwright


@pytest.fixture
def setup():
    with sync_playwright() as p:
        with allure.step("Launch the browser and navigate to the login page"):
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(
                "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
            )

        yield page

        with allure.step("Close the browser"):
            browser.close()