import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.driver_factory import get_driver

@pytest.fixture(scope="function")
def driver():
    """Create and return a WebDriver instance"""
    driver = get_driver()
    yield driver
    driver.quit() 