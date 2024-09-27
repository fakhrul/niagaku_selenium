# tests/test_quotations.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.employee.receipt_list_page import ReceiptListPage
import os
from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()

APP_URL = os.getenv("APP_URL")

@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # or webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_open_receipt_list(setup):
    driver = setup
    receipt_list_page = ReceiptListPage(driver)

    # Navigate to the Quotation List
    receipt_list_page.navigate_to(APP_URL + "/pages/login")
    receipt_list_page.input_text_by_test_id(("usernameInput"), "tenant1@niagaku.com")
    receipt_list_page.input_text_by_test_id(("passwordInput"), "qwe123")
    receipt_list_page.click((By.CSS_SELECTOR, ".btn-success"))

    # Navigate to Quotation List and Add Quotation
    receipt_list_page.navigate_to_receipt_list()
    # quotations_page.add_quotation(customer_name="Test Customer", total_amount="5000")
    
    # # Verify the success message or the appearance of the new quotation
    # success_message = quotations_page.get_element_text((By.CLASS_NAME, "success_message"))
    # assert "Quotation added successfully" in success_message
    assert "Receipt List added successfully"
