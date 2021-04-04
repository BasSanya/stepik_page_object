from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, ".basket-mini .btn-group a")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner>p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_FORM_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_FORM_BUTTON = (By.NAME, 'registration_submit')



class ProductPageLocators():
    PRODUCT_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME_IN_NOTIFICATION = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1) strong')
    PRODUCT_PRICE_IN_NOTIFICATION = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    PRODUCT_BASKET_BUTTON = (By.CSS_SELECTOR, '.alertinner p a:first-child')
    PRODUCT_BASKET_NAME = (By.CSS_SELECTOR, '.basket-items h3 a')
    PRODUCT_BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, '.table-condensed .total .price_color')
    PRODUCT_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
