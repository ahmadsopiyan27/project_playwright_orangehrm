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

    login_page.input_username()
    login_page.input_password()
    login_page.click_login_button()
    products_page.verify_dasboard()

# @allure.title("Negative Login Test")
# @allure.description("This test case is to verify the negative login functionality of the OrangeHRM application.")
# @allure.severity(allure.severity_level.NORMAL)
# @allure.tag("Login", "Negative Test")
# def test_negative_login(setup):
#     with sync_playwright() as p:
#         with allure.step("Enter invalid credentials and submit the login form"):
#             setup.locator("//input[@name='username']").fill("Admin")
#             setup.locator("//input[@name='password']").fill("asaaassdd")
#             setup.locator("//button[@type='submit']").click()
#         with allure.step("Verify the error message"):
#             assert setup.locator("//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text_content() == "Invalid credentials"
#         allure.attach(setup.screenshot(), name="Negative Login Screenshot", 
#                               attachment_type=allure.attachment_type.PNG)