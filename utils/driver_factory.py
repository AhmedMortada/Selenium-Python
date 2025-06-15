from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import yaml
import os

def get_driver():
    # Load configuration
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.yaml')
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    # Get environment settings
    env = os.getenv('ENV', 'dev')
    settings = config['environments'][env]
    
    # Setup Chrome options
    chrome_options = Options()
    if settings['headless']:
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-notifications')
    
    # Create and return driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(settings['implicit_wait'])
    return driver
