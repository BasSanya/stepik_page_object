from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'

    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')

    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    PRODUCT_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME_IN_NOTIFICATION = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1) strong')
    PRODUCT_PRICE_IN_NOTIFICATION = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    PRODUCT_BUSKET_BUTTON = (By.CSS_SELECTOR, '.alertinner p a:first-child')
    PRODUCT_BUSKET_NAME = (By.CSS_SELECTOR, '.basket-items h3 a')
    PRODUCT_BUSKET_TOTAL_PRICE = (By.CSS_SELECTOR, '.table-condensed .total .price_color')
