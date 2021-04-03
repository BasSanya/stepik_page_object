from .base_page import BasePage
from ..locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def add_to_basket(self):
         add_button = self.browser.find_element(*ProductPageLocators.PRODUCT_BUTTON)
         add_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def price_value(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def name_value(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def is_added_to_busket(self, price, name):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_NOTIFICATION).text == price, \
            "In busket added a product with wrong price"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_NOTIFICATION).text == name, \
            "In busket added wrong product"

    def go_to_busket(self):
        button = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_BUTTON)
        button.click()

    def is_correct_product_in_busket(self, price, name):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_NAME).text == name, \
            "Name in busket is not right!"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_TOTAL_PRICE).text == price, \
            "Price of product in busket is not right!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_after_some_time(self):
        assert  self.is_disappeared(*ProductPageLocators.PRODUCT_SUCCESS_MESSAGE), \
            "Success message is present, but should go away"