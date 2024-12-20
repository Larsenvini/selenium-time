from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Correctly set the path to your ChromeDriver
driver_path = "drivers/chromedriver"  # Adjust the path to your ChromeDriver

# Use the Service class to specify the driver path
service = Service(driver_path)

# Pass the service to the Chrome WebDriver
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://www.google.com")  # Open a website
    print("ChromeDriver is working!")
finally:
    driver.quit()  # Close the browser
