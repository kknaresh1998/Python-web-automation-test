from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

def test_sort(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    #driver.maximize_window()
    browserSortedList = []

    driver.find_element(By.XPATH, "(//th[@role='columnheader'])[1]").click()

    veggiesWebList = driver.find_elements(By.XPATH, "//tr//td[1]")

    for veggie in veggiesWebList:
        browserSortedList.append(veggie.text)

    ogSortedList = browserSortedList.copy()

    browserSortedList.sort()

    assert ogSortedList == browserSortedList