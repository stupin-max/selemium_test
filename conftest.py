import pytest
import random
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
# from fake_useragent import UserAgent


m_user_agent = f"Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (KHTML, как Gecko) Chrome / 81.0.4044.92 Safari / 537.36"
# proxy = ['93.123.226.23:81']

@pytest.fixture(scope="function")
def browser():
    #options
    path_to_driver = Service('./chromedriver.exe')
    options = webdriver.ChromeOptions()
    # user_agent = UserAgent()
    # options.add_argument(f"user-agent={user_agent.random}")
    options.add_argument(f"user-agent={m_user_agent}")
    options.add_argument(f"--disable-blink-features=AutomationControlled")
    # options.add_argument(f"--proxy-server={random.choice(proxy)}")
    #driver
    driver = webdriver.Chrome(service = path_to_driver, options = options)
    driver.maximize_window()
    yield driver
    driver.quit()
