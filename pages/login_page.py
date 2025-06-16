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
        self.PassWord=(By.ID,"Password")

    def click_login(self):
      self.driver.find_element(*self.ClickLogin).click()





    

    
       

    