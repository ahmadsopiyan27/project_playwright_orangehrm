from playwright.sync_api import sync_playwright
import pytest
import allure

@allure.title("Login Test")
@allure.description("This test case is to verify the login functionality of the OrangeHRM application.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Login", "Smoke Test")
def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        

        page.locator("//input[@name='username']").fill("Admin")
        page.locator("//input[@name='password']").fill("admin123")
        page.locator("//button[@type='submit']").click()
        assert page.locator("//h6[normalize-space()='Dashboard'][1]").text_content() == "Dashboard"

@allure.title("Negative Login Test")
@allure.description("This test case is to verify the negative login functionality of the OrangeHRM application.")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("Login", "Negative Test")
def test_negative_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        

        page.locator("//input[@name='username']").fill("Admin")
        page.locator("//input[@name='password']").fill("asaaassdd")
        page.locator("//button[@type='submit']").click()
        assert page.locator("//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text_content() == "Invalid credentials"
        browser.close() 