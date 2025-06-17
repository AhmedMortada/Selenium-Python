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