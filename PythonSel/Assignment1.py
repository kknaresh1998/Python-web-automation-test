import wait
from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(5)
driver.find_element(By.CLASS_NAME, "blinkingText").click()
windowOpen = driver.window_handles
driver.switch_to.window(windowOpen[1])
message = driver.find_element(By.CSS_SELECTOR, ".red").text
var = message.split("at")[1].strip().split(" ")[0]
driver.close()
driver.switch_to.window(windowOpen[0])
driver.find_element(By.ID,"username").send_keys(var)
driver.find_element(By.ID,"password").send_keys("XYZ123")
dropdowns = Select(driver.find_element(By.XPATH, "//select[@class='form-control']"))
dropdowns.select_by_visible_text("Student")
driver.find_element(By.ID,"signInBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//form/div[1]")))
print(driver.find_element(By.XPATH, "//form/div[1]").text)
