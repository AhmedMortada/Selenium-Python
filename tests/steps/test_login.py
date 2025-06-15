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

@given("the user is on the login page")
def user_on_login_page(driver):
    logger.info("Navigating to Google homepage")
    driver.get("https://www.google.com")
    return LoginPage(driver)

@when("the user accepts cookies")
def accept_cookies(login_page):
    logger.info("Accepting cookies")
    login_page.accept_cookies()

@when(parsers.parse('the user searches for "{search_term}"'))
def search_term(login_page, search_term):
    logger.info(f"Searching for: {search_term}")
    login_page.search(search_term)

# @then("the user able to search")
# def verify_search(login_page):
#     logger.info("Verifying search results")
#     assert login_page.is_search_successful(), "Search was not successful" 