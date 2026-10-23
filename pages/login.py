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

    def click_forget_password(self):
        with allure.step("Click on forget password link"):
            self.page.locator(Loc.forget_password).click()

    def input_reset_password_username(self, username):
        with allure.step("Enter username for reset password"):
            self.page.locator(Loc.reset_password_username).fill(username)

    def click_reset_password_button(self):
        with allure.step("Click reset password button"):
            self.page.locator(Loc.button_reset_password).click()

    def click_cancel_button(self):
        with allure.step("Click cancel button"):
            self.page.locator(Loc.button_cancel).click()


    def verify_success_reset_password(self, expected_text):
        with allure.step("Verify the success message for reset password"):
            success_message = self.page.locator(Loc.verify_success_reset_password)
            expect(success_message).to_have_text(expected_text)
            allure.attach(
                self.page.screenshot(),
                name="Reset Password Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    def login_homepage(self, login):
        with allure.step("Verify the login homepage"):
            homepage_text = self.page.locator(Loc.login_hompepage)
            expect(homepage_text).to_have_text(login)
            allure.attach(
                self.page.screenshot(),
                name="Login Homepage Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )