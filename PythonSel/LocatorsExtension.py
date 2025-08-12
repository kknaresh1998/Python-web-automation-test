import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://rahulshettyacademy.com/client/auth/login")
print(driver.title)
print(driver.current_url)
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//div/form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(3) input").send_keys("Hello@1234")
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()

