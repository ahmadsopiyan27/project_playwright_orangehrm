import allure
from playwright.sync_api import sync_playwright, expect
from locators.products import Loc

class products:
        def __init__(self, page):
            self.page = page

        def verify_dasboard(self):
            with allure.step("Verify the dashboard page is displayed"):
                assert self.page.locator(Loc.dashboard).text_content() == "Dashboard"
                allure.attach(self.page.screenshot(), name="Dashboard Screenshot", 
                attachment_type=allure.attachment_type.PNG)
