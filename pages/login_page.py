from .base_page import BasePage
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url == MainPageLocators.LOGIN_URL, "Current page is not a Login Page " + str(self.browser.current_url)

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*MainPageLocators.REGISTRATION_FORM), "Registration form is not present"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*MainPageLocators.REGISTRATION_FORM_EMAIL)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*MainPageLocators.REGISTRATION_FORM_PASSWORD)
        password_field.send_keys(password)

        password_confirm_field = self.browser.find_element(*MainPageLocators.REGISTRATION_FORM_PASSWORD_CONFIRM)
        password_confirm_field.send_keys(password)

        submit_registration_button = self.browser.find_element(*MainPageLocators.REGISTRATION_FORM_BUTTON)
        submit_registration_button.click()