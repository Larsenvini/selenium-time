from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to your ChromeDriver
driver_path = "drivers/chromedriver"
service = Service(driver_path)

# Set up the WebDriver
driver = webdriver.Chrome(service=service)

try:
    # Open the demo website
    driver.get("https://the-internet.herokuapp.com/")
    print("Opened demo website.")
    time.sleep(2)

    # Navigate to "Dynamic Loading"
    dynamic_loading = driver.find_element(By.LINK_TEXT, "Dynamic Loading")
    dynamic_loading.click()
    time.sleep(2)

    # Click on Example 1 to load dynamic content
    example_1 = driver.find_element(By.PARTIAL_LINK_TEXT, "Example 1")
    example_1.click()
    print("Navigated to Example 1.")
    time.sleep(2)

    # Start loading dynamic content
    start_button = driver.find_element(By.TAG_NAME, "button")
    start_button.click()
    print("Started loading dynamic content.")

    # Wait for the content to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "finish"))
    )
    print("Dynamic content loaded.")

    # Print the content of the loaded element
    loaded_content = driver.find_element(By.ID, "finish")
    print("Loaded content:", loaded_content.text)

finally:
    # Close the browser
    driver.quit()
