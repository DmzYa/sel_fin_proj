import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'no "login" link here !'


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is absent!'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Reg form is absent!'


    def register_new_user(self, email, password):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) +"fake"
        em_adrr = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        em_adrr.send_keys(email)
        psw1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS)
        psw1.send_keys(password)
        psw2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS_AGAIN)
        psw2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()