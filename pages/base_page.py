# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def wait_for_element(self, by_locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))

    def click(self, by_locator):
        self.wait_for_element(by_locator).click()

    # def click_by_test_id(self, by_locator):
    #     self.wait_for_element(by_locator).click()


    def input_text(self, by_locator, text):
        element = self.wait_for_element(by_locator)
        element.clear()
        element.send_keys(text)

    def input_text_by_test_id(self, id, text):
        element = self.driver.find_element(By.XPATH, "//*[@data-test-id=\""+id + "\"]")
        element.clear()
        element.send_keys(text)

    def get_element_text(self, by_locator):
        return self.wait_for_element(by_locator).text
