# pages/quotation_list_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class PurchaseQuotationListPage(BasePage):
    EXPENSES_MENU = (By.XPATH, '//a[contains(text(),"Expenses")]')  # Parent menu that needs to be expanded
    PURCHASE_QUOTATION_LIST_LINK = (By.XPATH, '//a[@href="/tenants/purchaseQuotationList"]')

    def navigate_to_purchase_quotation_list(self):
        # Step 1: Click to expand the "Incomes" menu if it's collapsed
        expenses_menu = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.EXPENSES_MENU)
        )
        expenses_menu.click()

        # Step 2: Wait for the Quotation List link to become visible
        purchase_quotation_list_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.PURCHASE_QUOTATION_LIST_LINK)
        )

        # Step 3: Click the Quotation List link
        purchase_quotation_list_link.click()
