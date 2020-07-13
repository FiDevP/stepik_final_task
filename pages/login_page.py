from .base_page import BasePage
from .locators import MainPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "invalid link"

    def should_be_login_form(self):
        assert self.browser.find_element(*MainPageLocators.LOGIN_FORM), "login form is missing"

    def should_be_register_form(self):
        assert self.browser.find_element(*MainPageLocators.REGISTER_FORM), "register form is missing"
