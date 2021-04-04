from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


class BasketPage(ProductPage):
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