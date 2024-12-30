from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Path to your ChromeDriver
driver_path = "drivers/chromedriver"
service = Service(driver_path)

# Set up the WebDriver
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Open the updated main page
    driver.get("https://seleniumplayground.practiceprobs.com/")
    print("Opened main page.")
    time.sleep(2)  # Allow time for the page to load

    # Step 2: Locate the search input field directly
    search_bar = driver.find_element(By.CSS_SELECTOR, "input.md-search__input")
    search_bar.send_keys("German Shepherd")
    print("Typed 'German Shepherd' in the search bar.")
    time.sleep(1)

    # Step 3: Simulate pressing Enter to submit the search query
    search_bar.send_keys(Keys.RETURN)
    print("Submitted search query using Enter key.")
    time.sleep(3)

    # Step 4: Locate the "Wikipedia, the free encyclopedia" link using XPath and click it
    wikipedia_link = driver.find_element(By.XPATH, "/html/body/div[3]/main/div/div[3]/article/p[1]/em/a")
    wikipedia_link.click()
    print("Clicked Wikipedia link.")
    time.sleep(2)

    # Step 5: Print the current page title to confirm navigation
    print("Navigated to page:", driver.title)

finally:
    # Close the browser
    driver.quit()

