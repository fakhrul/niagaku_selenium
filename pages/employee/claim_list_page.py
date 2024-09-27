# pages/quotation_list_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ClaimListPage(BasePage):
    CLAIM_LIST_LINK = (By.XPATH, '//a[@href="/employee/claimList"]')

    def navigate_to_claim_list(self):
        claim_list_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.CLAIM_LIST_LINK)
        )

        # Step 3: Click the Quotation List link
        claim_list_link.click()
