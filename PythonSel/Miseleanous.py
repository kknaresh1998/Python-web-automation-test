from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


# Set Firefox options
firefox_option = webdriver.FirefoxOptions()
firefox_option.add_argument("headless")
#firefox_option.headless = True  # Enable headless mode
firefox_option.add_argument("--ignore-certificate-errors")

# Correct placement of options
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_option)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

driver.execute_script("window.scrollBy(0, 700);")
driver.save_screenshot("screen.png")
