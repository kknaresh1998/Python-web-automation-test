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
driver.get("http://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(5)
# driver.switch_to.frame("mce_0_ifr")
# close_button = driver.find_element(By.CSS_SELECTOR, "button.tox-notification__dismiss")
# close_button.click()
# driver.find_element(By.ID,"tinymce").clear()
# driver.find_element(By.ID,"tinymce").send_keys("Hello world!")
# driver.switch_to.default_content()
# print(driver.find_element(By.TAG_NAME,"h3").text)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/iframe")

# Switch into the iFrame
iframe = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(iframe)

# Wait for and close the alert
wait = WebDriverWait(driver, 10)
close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.tox-notification__dismiss")))
action = ActionChains(driver)
action.move_to_element(close_button).click().perform()

# Type text in the editor
editor = driver.find_element(By.ID, "tinymce")
editor.clear()
editor.send_keys("Hello iFrame!")

# Switch back to main page
driver.switch_to.default_content()

# Wait for and close the alert
wait = WebDriverWait(driver, 10)
close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.tox-notification__dismiss")))
action = ActionChains(driver)
action.move_to_element(close_button).click().perform()

# Do other actions...


