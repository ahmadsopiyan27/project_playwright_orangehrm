import allure
from playwright.sync_api import sync_playwright, expect
from locators.login import Loc


class LoginPage:

    def __init__(self, page):
        self.page = page


    def input_username(self, username):
        with allure.step("Enter valid username"):
            self.page.locator(Loc.username).fill(username)

    def input_password(self, password):
        with allure.step("Enter valid password"):
            self.page.locator(Loc.password).fill(password)

    def click_login_button(self):
        with allure.step("Click login button"):
            self.page.locator(Loc.login_button).click()

    def verify_invalid_credential_error(self):
        with allure.step("Verify the error message"):
            error = self.page.locator("//p[contains(@class,'oxd-alert-content-text')]")
            assert error.text_content() == "Invalid credentials"
            allure.attach(
                self.page.screenshot(),
                name="Negative Login Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )