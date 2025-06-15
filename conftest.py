import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to run tests: chrome or firefox")

@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="function")
def driver(browser_type):
    if browser_type.lower() == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_type.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    else:
        raise ValueError(f"Browser {browser_type} is not supported")
    
    yield driver
    driver.quit() 