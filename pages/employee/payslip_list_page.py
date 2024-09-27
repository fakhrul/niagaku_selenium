# pages/quotation_list_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class EmployeePaySlipListPage(BasePage):
    EMPLOYEE_PAYSLIP_LIST_LINK = (By.XPATH, '//a[@href="/employee/paySlipList"]')

    def navigate_to_employee_payslip_list(self):
        employee_payslip_list_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.EMPLOYEE_PAYSLIP_LIST_LINK)
        )

        # Step 3: Click the Quotation List link
        employee_payslip_list_link.click()
