# pages/quotation_list_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ProductListPage(BasePage):
    INCOMES_MENU = (By.XPATH, '//a[contains(text(),"Incomes")]')  # Parent menu that needs to be expanded
    PRODUCT_LIST_LINK = (By.XPATH, '//a[@href="/tenants/productList"]')

    def navigate_to_product_list(self):
        # Step 1: Click to expand the "Incomes" menu if it's collapsed
        incomes_menu = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.INCOMES_MENU)
        )
        incomes_menu.click()

        # Step 2: Wait for the Quotation List link to become visible
        product_list_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.PRODUCT_LIST_LINK)
        )

        # Step 3: Click the Quotation List link
        product_list_link.click()
