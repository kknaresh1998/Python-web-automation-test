from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from  selenium.webdriver.edge.service import Service as EdgeService


#driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver =webdriver.Edge(service=EdgeService(executable_path="C:\Program Files\grid\Webdrivers\msedgedriver.exe"))
driver.get("https://www.google.com")