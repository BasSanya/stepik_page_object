from .base_page import BasPage
from selenium.webdriver.common.by import By

class MainPage(BasPage):
    def go_to_login_page(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"