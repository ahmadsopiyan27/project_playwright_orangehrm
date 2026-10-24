import allure
import pytest
from pages.login import LoginPage
from pages.dashboard import DashboardPage
from locators.dashboard import Loc

SIDEBAR_MENUS = {
    "Admin": "/admin/",
    "PIM": "/pim/viewEmployeeList",
    "Leave": "/leave/",
    "Time": "/time/",
    "Recruitment": "/recruitment/",
    "My Info": "/pim/viewPersonalDetails",
    "Performance": "/performance/",
    "Dashboard": "/dashboard/",
    "Directory": "/directory/",
    "Claim": "/claim/",
    "Buzz": "/buzz/",
}


@allure.title("Dashboard Widget Test")
@allure.description("DSH-001: Verify the dashboard widgets are displayed.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Dashboard", "Smoke Test")
def test_dsh_001_dashboard_widget(setup):
    login_page = LoginPage(setup)
    dashboard_page = DashboardPage(setup)

    login_page.input_username("Admin")
    login_page.input_password("admin123")
    login_page.click_login_button()
    dashboard_page.verify_widgets_displayed([
        Loc.widget_time_at_work,
        Loc.widget_my_actions,
        Loc.widget_quick_launch,
        Loc.widget_employee_distribution,
    ])


@allure.title("Sidebar Navigation Test")
@allure.description("DSH-002: Verify each sidebar menu opens the correct page without error.")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("Dashboard", "Navigation Test")
@pytest.mark.parametrize("menu, url_path", SIDEBAR_MENUS.items())
def test_dsh_002_sidebar_navigation(setup, menu, url_path):
    login_page = LoginPage(setup)
    dashboard_page = DashboardPage(setup)

    login_page.input_username("Admin")
    login_page.input_password("admin123")
    login_page.click_login_button()
    dashboard_page.click_sidebar_menu(menu)
    dashboard_page.verify_page_opened(url_path)


@allure.title("Sidebar Search Test")
@allure.description("DSH-003: Verify sidebar search only shows menus matching the keyword.")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("Dashboard", "Search Test")
def test_dsh_003_sidebar_search(setup):
    login_page = LoginPage(setup)
    dashboard_page = DashboardPage(setup)

    login_page.input_username("Admin")
    login_page.input_password("admin123")
    login_page.click_login_button()
    dashboard_page.input_sidebar_search("PIM")
    dashboard_page.verify_sidebar_search_result("PIM")