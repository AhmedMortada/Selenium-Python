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

@given('the user is on the login page')
def go_to_login_page(driver):
    driver.get("https://www.google.com/")
    # Wait for page to load
    driver.implicitly_wait(5)

@when('the user accepts cookies')
def accept_cookies(driver, login_page):
    assert login_page.accept_cookies(), "Failed to handle cookies"

@when(parsers.parse('the user searches for "{search_text}"'))
def search_text(driver, login_page, search_text):
    login_page.search(search_text)