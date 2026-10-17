import allure
from playwright.sync_api import sync_playwright, expect
from locators.login import Loc


class LoginPage:

    def __init__(self, page):
        self.page = page


    def input_username(self):
        with allure.step("Enter valid username"):
            self.page.locator(Loc.username).fill("Admin")

    def input_password(self):
        with allure.step("Enter valid password"):
            self.page.locator(Loc.password).fill("admin123")

    def click_login_button(self):
        with allure.step("Click login button"):
            self.page.locator(Loc.login_button).click()