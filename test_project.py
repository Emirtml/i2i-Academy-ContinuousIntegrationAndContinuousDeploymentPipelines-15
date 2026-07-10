import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tax_calculator import calculate_telecom_tax

# 1. Unit Test for telecom tax function
def test_telecom_tax_calculation():
    # If amount is 100, tax must be 15
    result = calculate_telecom_tax(100)
    assert result == 15.0

# 2. Selenium UI Test in headless mode
def test_website_ui_loads():
    # Configure Chrome to run in headless mode (no visual screen)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Start the Chrome browser with options
    driver = webdriver.Chrome(options=chrome_options)
    
    # Navigate to a public website
    driver.get("https://www.google.com")
    
    # Check if the page title contains "Google"
    assert "Google" in driver.title
    
    # Close the browser session
    driver.quit()