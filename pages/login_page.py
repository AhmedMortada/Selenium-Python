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

    def accept_cookies(self):
        """Click the accept cookies button"""
        try:
            logger.debug("Waiting for accept cookies button")
            # First check if the cookie dialog is present
            try:
                button = self.wait.until(
                    EC.element_to_be_clickable(self.COOKIE_ACCEPT)
                )
                button.click()
                logger.info("Successfully clicked accept cookies button")
            except TimeoutException:
                logger.info("No cookie dialog found, continuing...")
                return True
        except Exception as e:
            logger.error(f"Failed to handle cookies: {str(e)}")
            return False
        return True

    def search(self, text):
        """Simple search method with wait"""
        try:
            logger.debug("Finding search box")
            # Wait for search box to be present and visible
            search_box = self.wait.until(
                EC.presence_of_element_located(self.SEARCH_BOX)
            )
            search_box.clear()
            search_box.send_keys(text)
            logger.info(f"Entered search text: {text}")
            search_box.submit()
            logger.info("Submitted search")
            # Wait for search results
            time.sleep(2)  # Keep small wait for stability
        except Exception as e:
            logger.error(f"Search failed: {str(e)}")
            raise

    

    
       

    