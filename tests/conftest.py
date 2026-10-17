from playwright.sync_api import sync_playwright, expect
import pytest
import allure


@pytest.fixture
def setup():
    with allure.step("Launch the browser and navigate to the login page"):
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    yield browser

    with allure.step("Close the browser"):
        browser.close() 