# pages/quotation_list_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class PaySlipListPage(BasePage):
    PAYROLL_MENU = (By.XPATH, '//a[contains(text(),"Payroll")]')  # Parent menu that needs to be expanded
    PAYSLIP_LIST_LINK = (By.XPATH, '//a[@href="/tenants/paySlipList"]')

    def navigate_to_payslip_list(self):
        # Step 1: Click to expand the "Incomes" menu if it's collapsed
        payroll_menu = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.PAYROLL_MENU)
        )
        payroll_menu.click()

        # Step 2: Wait for the Quotation List link to become visible
        payslip_list_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.PAYSLIP_LIST_LINK)
        )

        # Step 3: Click the Quotation List link
        payslip_list_link.click()
