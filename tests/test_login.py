import allure
from pages.login import LoginPage
from pages.products import products


@allure.title("Logout Test")
@allure.description("This test case is to verify the logout functionality of the OrangeHRM application.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Login", "Smoke Test")
def test_logout(setup):

    login_page = LoginPage(setup)
    products_page = products(setup)

    login_page.input_username("Admin")
    login_page.input_password("admin123")
    login_page.click_login_button()
    login_page.click_profile_icon()
    login_page.click_logout_button()
    login_page.login_homepage("Login")

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


@allure.title("Reset Password Test")
@allure.description("This test case is to verify the reset password functionality of the OrangeHRM application.")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("Login", "Reset Password Test")
def test_reset_password(setup):
    login_page = LoginPage(setup)

    login_page.click_forget_password()
    login_page.input_reset_password_username("Adminn")
    login_page.click_reset_password_button()
    login_page.verify_success_reset_password("Reset Password link sent successfully")


@allure.title("Cancel Reset Password Test")
@allure.description("This test case is to verify the cancel reset password functionality of the OrangeHRM application.")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("Login", "Cancel Reset Password Test")
def test_cancel_reset_password(setup):
    login_page = LoginPage(setup)

    login_page.click_forget_password()
    login_page.input_reset_password_username("Adminn")
    login_page.click_cancel_button()
    login_page.login_homepage("Login")

@allure.title("Required Field Validation Test")
@allure.description("This test case is to verify the required field validation functionality of the OrangeHRM application.")
@allure.severity(allure.severity_level.NORMAL)  
@allure.tag("Login", "Required Field Validation Test")
def test_required_field_validation(setup):
    login_page = LoginPage(setup)

    login_page.click_login_button()
    login_page.verify_required_message(2)