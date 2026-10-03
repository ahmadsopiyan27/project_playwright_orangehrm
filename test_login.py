from playwright.sync_api import sync_playwright
import pytest
import allure

@allure.title("Login Test")
@allure.description("This test case is to verify the login functionality of the OrangeHRM application.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Login", "Smoke Test")
def test_login_success():
    with sync_playwright() as p:
        with allure.step("Launch the browser and navigate to the login page"):
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        with allure.step("Enter valid credentials and submit the login form"):
            page.locator("//input[@name='username']").fill("Admin")
            page.locator("//input[@name='password']").fill("admin123")
            page.locator("//button[@type='submit']").click()
        allure.attach(page.screenshot(), name="Login Success Screenshot", 
                      attachment_type=allure.attachment_type.PNG)
        assert page.locator("//h6[normalize-space()='Dashboard'][1]").text_content() == "Dashboard"

@allure.title("Negative Login Test")
@allure.description("This test case is to verify the negative login functionality of the OrangeHRM application.")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("Login", "Negative Test")
def test_negative_login():
    with sync_playwright() as p:
        with allure.step("Launch the browser and navigate to the login page"):
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        with allure.step("Enter invalid credentials and submit the login form"):
            page.locator("//input[@name='username']").fill("Admin")
            page.locator("//input[@name='password']").fill("asaaassdd")
            page.locator("//button[@type='submit']").click()
        allure.attach(page.screenshot(), name="Negative Login Screenshot", 
                      attachment_type=allure.attachment_type.PNG)
        with allure.step("Verify the error message"):
            assert page.locator("//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text_content() == "Invalid credentials"
        browser.close() 