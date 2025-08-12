import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CLASS_NAME,"search-keyword").send_keys("ber")
time.sleep(5)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count>0
print(count)

# assignment
expectedProductList =["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actualList= []


for result in results:
    result.find_element(By.XPATH,"div/button").click()
    actualList.append(result.find_element(By.XPATH,"h4").text)

assert expectedProductList == actualList

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

#Sum Validation
prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)
totalAmt = int(driver.find_element(By.XPATH,"//span[@class='totAmt']").text)

assert  sum == totalAmt

#Assignment

discountAmt = float(driver.find_element(By.XPATH,"//span[@class='discountAmt']").text)

assert discountAmt < totalAmt

