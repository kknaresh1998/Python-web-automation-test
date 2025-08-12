from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/windows")
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowOpen = driver.window_handles
driver.switch_to.window(windowOpen[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()
driver.switch_to.window(windowOpen[0])
print(driver.find_element(By.TAG_NAME,"h3").text)

