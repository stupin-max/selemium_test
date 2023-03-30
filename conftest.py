import pytest
import random
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import logging

def log():
    """ Logger setup"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(f"out.log", mode='w')
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


@pytest.fixture(scope="session")
def browser():

    logger = log()
    #options
    logger.info(f"Start option preparation")

    path_to_driver = Service('./chromedriver.exe')
    m_user_agent = f"Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (KHTML, как Gecko) Chrome / 81.0.4044.92 Safari / 537.36"
    options = webdriver.ChromeOptions()

    options.add_argument(f"user-agent={m_user_agent}")
    options.add_argument(f"--disable-blink-features=AutomationControlled")

    #driver
    try:
        driver = webdriver.Chrome(service = path_to_driver, options = options)
        driver.maximize_window()
        logger.info(f"Driver is ready")
    except Exception as err:
        logger.error(f"Problem with  driver: {err}")
    logger.info(f"Start testing")
    yield driver
    logger.info(f"Tests finished")
    driver.quit()
