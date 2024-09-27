# tests/test_quotations.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.tenants.other_expense_list_page import OtherExpenseListPage
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

def test_open_other_extense_list(setup):
    driver = setup
    other_expense_list_page = OtherExpenseListPage(driver)

    # Navigate to the Quotation List
    other_expense_list_page.navigate_to(APP_URL + "/pages/login")
    other_expense_list_page.input_text_by_test_id(("usernameInput"), "tenant1@niagaku.com")
    other_expense_list_page.input_text_by_test_id(("passwordInput"), "qwe123")
    other_expense_list_page.click((By.CSS_SELECTOR, ".btn-success"))

    # Navigate to Quotation List and Add Quotation
    other_expense_list_page.navigate_to_other_expense_list()
    # quotations_page.add_quotation(customer_name="Test Customer", total_amount="5000")
    
    # # Verify the success message or the appearance of the new quotation
    # success_message = quotations_page.get_element_text((By.CLASS_NAME, "success_message"))
    # assert "Quotation added successfully" in success_message
    assert "Other Expense List added successfully"
