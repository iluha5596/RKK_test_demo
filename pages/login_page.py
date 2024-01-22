import time
from pages.base_page import BasePage
from locators.login_locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    def authorization(self, login, password):
        input_login = self.driver.find_element(*LoginPageLocators.LOGIN_LINK)
        input_password = self.driver.find_element(*LoginPageLocators.PASSWORD_LINK)
        button_login = self.driver.find_element(*LoginPageLocators.BUTTON_LOGIN)
        input_login.send_keys(login)
        input_password.send_keys(password)
        button_login.click()

