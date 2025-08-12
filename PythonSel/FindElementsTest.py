import time

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium import webdriver

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item']")
for country in countries:
    if country.text == "India":
        country.click()
        break
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"



