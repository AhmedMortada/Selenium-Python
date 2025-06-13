from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage

scenarios('../login.feature')

@given('the user is on the login page')
def go_to_login_page(driver):
    driver.get("https://www.google.com/")

# @when('the user enters valid credentials')
# def enter_credentials(driver):
#     login_page = LoginPage(driver)
#     login_page.login('user', 'pass')

# @then('the user should be redirected to the dashboard')
# def verify_login(driver):
#     assert "dashboard" in driver.current_url
