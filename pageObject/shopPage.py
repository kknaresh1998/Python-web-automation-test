from selenium.webdriver.common.by import By
from pageObject.checkoutPage import Checkout_Confirmation
from util.browserUtil import BrowserUtils


class ShopPage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.XPATH, "(//a[@class='nav-link'])[2]")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.cart_link = (By.XPATH, "//a[@class='nav-link btn btn-primary']")


    def add_product_to_cart(self, productName):

        self.driver.find_element(*self.shop_link).click()
        self.driver.execute_script("window.scroll(0, 700);")
        productList = self.driver.find_elements(*self.product_cards)

        for product in productList:
            productText = product.find_element(By.XPATH, "div/h4/a").text

            if productText == productName:
                product.find_element(By.XPATH, "div/button").click()


    def go_to_Cart(self):
        self.driver.find_element(*self.cart_link).click()
        checkout = Checkout_Confirmation(self.driver)
        return checkout

