from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pageObject.shopPage import ShopPage
from util.browserUtil import BrowserUtils


class LoginPage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.sign_button = (By.ID, "signInBtn")
        self.loginStatus = (By.CSS_SELECTOR, ".alert-danger")


    def login(self, userName, password):
        self.driver.find_element(*self.username_input).send_keys(userName)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.sign_button).click()
        # wait = WebDriverWait(self.driver ,10)
        # loginError =wait.until(expected_conditions.visibility_of_element_located(self.loginStatus))
        # if "incorrect" in loginError.text:
        #     print("login failed")
        shop_page = ShopPage(self.driver)
        return shop_page
        # * mark is for separating tuple variable into two arrguments


