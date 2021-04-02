import pytest

from .pages.product_page import ProductPage
import time


def test_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    prod = ProductPage(browser, link)
    prod.open()
    prod.add_to_basket()
    prod.solve_quiz_and_get_code()
    name = prod.name_value()
    price = prod.price_value()
    prod.is_added_to_busket(price, name)
    prod.go_to_busket()
    prod.is_correct_product_in_busket(price, name)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    prod = ProductPage(browser, link)
    prod.open()
    prod.add_to_basket()
    prod.solve_quiz_and_get_code()
    prod.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    prod = ProductPage(browser, link)
    prod.open()
    prod.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    prod = ProductPage(browser, link)
    prod.open()
    prod.add_to_basket()
    prod.solve_quiz_and_get_code()
    prod.should_not_be_success_message_after_some_time()