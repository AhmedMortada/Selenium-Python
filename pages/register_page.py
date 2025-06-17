from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from utils.logger import get_logger

logger = get_logger()


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Define locators
        self.COOKIE_ACCEPT = (By.ID, "L2AGLb")  # Updated cookie button ID
        self.SEARCH_BOX = (By.NAME, "q")  # Using name instead of class
        self.SEARCH_RESULTS = (By.ID, "search")  # Search results container
        self.ClickLogin = (By.CLASS_NAME, "ico-login")
        self.UserName = (By.ID, "Email")
        self.PassWord = (By.ID, "Password")
        self.LoginButton = (By.XPATH, "//input[@value='Log in']")

    def click_login(self):
        self.driver.find_element(*self.ClickLogin).click()

    def enter_username(self, username):
        self.wait.until(EC.element_to_be_clickable(self.UserName))
        self.driver.find_element(*self.UserName).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PassWord))
        self.driver.find_element(*self.PassWord).send_keys(password)

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LoginButton))
        self.driver.find_element(*self.LoginButton).click()
        time.sleep(5)

    def is_logged_in(self):
        self.wait.until(EC.element_to_be_clickable(self.LoginButton))
        return self.driver.find_element(*self.LoginButton).is_enabled()











