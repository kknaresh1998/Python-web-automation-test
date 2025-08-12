from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element(By.XPATH,"(//a[@class='nav-link'])[2]").click()
driver.execute_script("window.scroll(0, 700);")
productList = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in productList:
    productText = product.find_element(By.XPATH, "div/h4/a").text

    if productText == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("Ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@class='btn btn-success btn-lg']").click()
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert-success")))
successText = driver.find_element(By.CSS_SELECTOR,".alert-success").text
assert "Success! Thank you! " in successText
driver.close()