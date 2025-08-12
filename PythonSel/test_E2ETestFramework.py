import json
import sys
import os

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObject.loginPage import LoginPage
from pageObject.shopPage import ShopPage
test_data_path ='../data/test_E2ETestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"] # convert json file into a data list

@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    shop_page = loginPage.login(test_list_item["userName"], test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["productName"])
    print(shop_page.getTitle())
    checkout = shop_page.go_to_Cart()
    checkout.product_checkout()
    checkout.enter_delivery_address("ind")
    checkout.validate_order()



