import allure
from pages.login import LoginPage
from pages.products import products


@allure.title("Login Test")
@allure.description("This test case is to verify the login functionality of the OrangeHRM application.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Login", "Smoke Test")
def test_login_success(setup):

    login_page = LoginPage(setup)
    products_page = products(setup)

    login_page.input_username("Admin")
    login_page.input_password("admin123")
    login_page.click_login_button()
    products_page.verify_dasboard()

@allure.title("Negative Login Test")
@allure.description("This test case is to verify the negative login functionality of the OrangeHRM application.")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("Login", "Negative Test")
def test_negative_login(setup):
    login_page = LoginPage(setup)

    login_page.input_username("assddssds")
    login_page.input_password("wrongpassword")
    login_page.click_login_button()
    login_page.verify_invalid_credential_error()