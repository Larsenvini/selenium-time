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
    # Step 1: Open the demo website for JavaScript alerts
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    print("Opened JavaScript alerts demo page.")
    time.sleep(2)

    # Step 2: Handle a simple alert
    alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    alert_button.click()
    print("Clicked simple alert button.")
    time.sleep(1)

    # Switch to the alert and accept it
    alert = driver.switch_to.alert
    print("Alert text:", alert.text)
    alert.accept()
    print("Accepted the alert.")

    # Step 3: Handle a confirmation alert
    confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
    confirm_button.click()
    print("Clicked confirmation alert button.")
    time.sleep(1)

    # Switch to the confirmation alert and dismiss it
    confirm_alert = driver.switch_to.alert
    print("Confirmation alert text:", confirm_alert.text)
    confirm_alert.dismiss()
    print("Dismissed the confirmation alert.")

    # Step 4: Handle a prompt alert
    prompt_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
    prompt_button.click()
    print("Clicked prompt alert button.")
    time.sleep(1)

    # Switch to the prompt alert, enter text, and accept it
    prompt_alert = driver.switch_to.alert
    print("Prompt alert text:", prompt_alert.text)
    prompt_alert.send_keys("Hello Selenium!")
    prompt_alert.accept()
    print("Accepted the prompt alert with input.")

finally:
    # Close the browser
    driver.quit()
