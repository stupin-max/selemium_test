from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage():

    """ Yandex main page general functions"""

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ya.ru/"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_url(self):
        return self.driver.current_url

    def switch_to_new_tab(self):
        all_id = self.driver.window_handles
        return self.driver.switch_to.window(all_id[1])

    def check_if_dlisplayed(self, locator):
        return locator.is_displayed()

    def find_element(self, locator,time=30):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=30):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def move_to_element(self, locator):
        action = ActionChains(self.driver)
        return action.move_to_element(locator).click(locator).perform()


class ImagePage():

    """ Yandex Image page general functions"""

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://yandex.ru/images/"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_url(self):
        return self.driver.current_url

    def switch_to_new_tab(self):
        all_id = self.driver.window_handles
        return self.driver.switch_to.window(all_id[1])

    def check_if_dlisplayed(self, locator):
        return locator.is_displayed()

    def find_element(self, locator,time=30):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=30):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def move_to_element(self, locator):
        action = ActionChains(self.driver)
        return action.move_to_element(locator).click(locator).perform()
