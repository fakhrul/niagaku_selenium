# pages/quotation_list_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ReceiptListPage(BasePage):
    RECEIPT_LIST_LINK = (By.XPATH, '//a[@href="/employee/receiptList"]')

    def navigate_to_receipt_list(self):
        receipt_list_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.RECEIPT_LIST_LINK)
        )

        # Step 3: Click the Quotation List link
        receipt_list_link.click()
