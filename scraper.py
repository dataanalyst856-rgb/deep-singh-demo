from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the driver
driver = webdriver.Chrome()

try:
    # Navigate to a website
    driver.get("https://example.com")
    
    # Wait for an element to load (max 10 seconds)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "h1"))
    )
    
    # Extract data
    print(element)
    
finally:
    # Always close the driver
    driver.quit()