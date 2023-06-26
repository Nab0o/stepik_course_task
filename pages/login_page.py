from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import time
import pytest

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert '/login/' in self.browser.current_url, 'Login url is not found'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not present'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.register_form), 'Register form is not present'
    
    def register_new_user(self, email, password):
        #self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        #self.should_be_login_page
        enteremail = self.browser.find_element(*LoginPageLocators.register_email)
        enteremail.send_keys(email)
        enterpassword = self.browser.find_element(*LoginPageLocators.register_password)
        enterpassword.send_keys(password)
        enterpassword2 = self.browser.find_element(*LoginPageLocators.register_password_confirm)
        enterpassword2.send_keys(password)  
        submitbtn = self.browser.find_element(*LoginPageLocators.button_confirm_registration)
        submitbtn.click()
