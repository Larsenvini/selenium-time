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
    # Open the website
    driver.get("https://seleniumplayground.netlify.app/")
    time.sleep(2)

    # Locate the <h1> using XPath by text
    heading_xpath = driver.find_element(By.XPATH, "//h1[text()='Selenium Playground']")
    print("Heading text (XPath - Text):", heading_xpath.text)

    # Locate the <h1> using CSS Selector by tag
    heading_css = driver.find_element(By.CSS_SELECTOR, "h1")
    print("Heading text (CSS - Tag):", heading_css.text)

finally:
    # Close the browser
    driver.quit()
