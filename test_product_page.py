import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time

@pytest.mark.login
class TestLoginFromProductPage():
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
        prod = BasketPage(browser, link)
        prod.open()
        prod.add_to_basket()
        prod.solve_quiz_and_get_code()
        name = prod.name_value()
        price = prod.price_value()
        prod.is_added_to_busket(price, name)
        prod.go_to_busket()
        prod.is_correct_product_in_busket(price, name)

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
        prod = BasketPage(browser, link)
        prod.open()
        prod.add_to_basket()
        prod.solve_quiz_and_get_code()
        prod.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
        prod = ProductPage(browser, link)
        prod.open()
        prod.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
        prod = BasketPage(browser, link)
        prod.open()
        prod.add_to_basket()
        prod.solve_quiz_and_get_code()
        prod.should_not_be_success_message_after_some_time()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
        prod = BasketPage(browser, link)
        prod.open()
        prod.view_basket()
        prod.is_basket_empty()

@pytest.mark.login_product_test
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        self.prod = BasketPage(browser, link)
        self.prod.open()
        self.prod.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = 'P6r772VdvB'
        self.prod.register_new_user(email, password)
        self.prod.should_be_authorized_user()
        browser.back()
        browser.back()

    def test_user_cant_see_success_message (self):
        self.prod.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket (self):
        self.prod.add_to_basket()
        self.prod.solve_quiz_and_get_code()
        name = self.prod.name_value()
        price = self.prod.price_value()
        self.prod.is_added_to_busket(price, name)
        self.prod.go_to_busket()
        self.prod.is_correct_product_in_busket(price, name)