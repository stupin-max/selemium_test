from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ya.ru/"

    def find_element(self, locator,time=30):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=30):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_url(self):
        return self.driver.current_url

    def switch_to_new_tab(self):
        all_id = self.driver.window_handles
        return self.driver.switch_to.window(all_id[1])

class ImagePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://yandex.ru/images/"

    def move_to_element(self, locator):
        action = ActionChains(self.driver)
        return action.move_to_element(locator).click(locator).perform()
