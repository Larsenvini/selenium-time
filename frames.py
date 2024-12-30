from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Path to your ChromeDriver
driver_path = "drivers/chromedriver"
service = Service(driver_path)

# Set up the WebDriver
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Open the demo website with multiple frames
    driver.get("https://the-internet.herokuapp.com/nested_frames")
    print("Opened nested frames demo page.")
    time.sleep(2)

    # Switch to the top frame and the middle frame
    driver.switch_to.frame("frame-top")
    driver.switch_to.frame("frame-middle")
    print("Switched to middle frame.")
    middle_text = driver.find_element(By.ID, "content").text
    print("Middle frame content:", middle_text)

    # Switch back to the main content
    driver.switch_to.default_content()
    print("Switched back to main content.")

    # Verify actions on the main page
    page_header = driver.find_element(By.TAG_NAME, "h3").text
    print("Main page header:", page_header)

finally:
    # Close the browser
    driver.quit()
