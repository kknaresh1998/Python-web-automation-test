import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

#driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()

#driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys("Naresh")
driver.find_element(By.XPATH,"(//input[@name='email'])[1]").send_keys("kknaresh1998@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
#driver.find_element(By.XPATH,"(//input[@id='inlineRadio2'])[1]").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
wait = WebDriverWait(driver, 5)
# success_message = wait.until(
#      EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))).text
message: str = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "success" in message
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("hello again")



time.sleep(2)