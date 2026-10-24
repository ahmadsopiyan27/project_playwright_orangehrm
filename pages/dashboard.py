import re
import allure
from playwright.sync_api import expect
from locators.dashboard import Loc


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def verify_widgets_displayed(self, widgets):
        with allure.step("Verify dashboard widgets are displayed"):
            for widget in widgets:
                expect(self.page.locator(widget)).to_be_visible()
            allure.attach(
                self.page.screenshot(),
                name="Dashboard Widgets Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    def click_sidebar_menu(self, name):
        with allure.step(f"Click sidebar menu '{name}'"):
            self.page.locator(Loc.sidebar_menu(name)).click()

    def verify_page_opened(self, url_path):
        with allure.step(f"Verify page opened without error ({url_path})"):
            expect(self.page).to_have_url(re.compile(url_path))
            expect(self.page.locator(Loc.page_header)).to_be_visible()
            allure.attach(
                self.page.screenshot(),
                name=f"Page {url_path} Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    def input_sidebar_search(self, keyword):
        with allure.step(f"Search sidebar menu with keyword '{keyword}'"):
            self.page.locator(Loc.sidebar_search).fill(keyword)

    def verify_sidebar_search_result(self, keyword):
        with allure.step(f"Verify only menus matching '{keyword}' are displayed"):
            menus = self.page.locator(Loc.sidebar_menu_items)
            expect(menus.first).to_be_visible()
            names = menus.all_inner_texts()
            assert len(names) > 0, "Tidak ada menu yang tampil"
            for name in names:
                assert keyword.lower() in name.lower(), f"'{name}' tidak sesuai keyword"
            allure.attach(
                self.page.screenshot(),
                name="Sidebar Search Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )