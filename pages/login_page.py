from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils.logger import get_logger

logger = get_logger()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Define locators
        self.COOKIE_ACCEPT = (By.ID, "W0wltc")
        self.SEARCH_BOX = (By.CLASS_NAME, "gLFyf")
          # Google accept cookies button

    def accept_cookies(self):
        """Click the accept cookies button"""
        try:
            logger.debug("Waiting for accept cookies button")
            button = self.wait.until(
                EC.element_to_be_clickable(self.COOKIE_ACCEPT)
            )
            button.click()
            logger.info("Successfully clicked accept cookies button")
        except Exception as e:
            logger.error(f"Failed to click accept cookies button: {str(e)}")
            print("Accept cookies button not found or not clickable")

    def search(self, text):
        """Simple search method with wait"""
        try:
            logger.debug("Finding search box")
            search_box = self.driver.find_element(*self.SEARCH_BOX)
            search_box.clear()
            search_box.send_keys(text)
            logger.info(f"Entered search text: {text}")
            search_box.submit()
            logger.info("Submitted search")
            time.sleep(2)  # Reduced wait time to 2 seconds
        except Exception as e:
            logger.error(f"Search failed: {str(e)}")
            raise

    def is_search_successful(self):
        try:
            self.wait.until(
                EC.presence_of_element_located((By.ID, "search"))
            )
            return True
        except:
            return False

    

    
       

    