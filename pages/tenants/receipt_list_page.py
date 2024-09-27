# pages/quotation_list_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ReceiptListPage(BasePage):
    EXPENSES_MENU = (By.XPATH, '//a[contains(text(),"Expenses")]')  # Parent menu that needs to be expanded
    RECEIPT_LIST_LINK = (By.XPATH, '//a[@href="/tenants/receiptList"]')

    def navigate_to_receipt_list(self):
        # Step 1: Click to expand the "Incomes" menu if it's collapsed
        expenses_menu = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.EXPENSES_MENU)
        )
        expenses_menu.click()

        # Step 2: Wait for the Quotation List link to become visible
        receipt_list_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.RECEIPT_LIST_LINK)
        )

        # Step 3: Click the Quotation List link
        receipt_list_link.click()
