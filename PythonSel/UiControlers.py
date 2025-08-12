from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
name = "Naresh"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radioButton = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radioButton[2].click()
assert radioButton[2].is_selected()

driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()

#MouseOver
element = driver.find_element(By.ID,"mousehover")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
action = ActionChains(driver)
action.scroll_to_element(element).perform()
action.move_to_element(element).click().perform()
action.context_click(element).perform()