import pytest
from pytest_bdd import given, when, then, parsers, scenarios
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

logger = get_logger()

# Link the feature file
scenarios('../../features/login.feature')

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@given('the user is on the Shop Page')
def go_to_login_page(driver):
    driver.get("https://demowebshop.tricentis.com/")
    # Wait for page to load
    driver.implicitly_wait(5)

@when('the user clicks the login button')
def click_login_button(login_page):
    login_page.click_login()

@when('the user enters the username')
def enter_username(login_page):
    login_page.enter_username("testuser@example.com")

@when('the user enters the password')
def enter_password(login_page):
    login_page.enter_password("testpassword")

@when('the user clicks the login button')
def click_login_button(login_page):
    login_page.click_login_button()