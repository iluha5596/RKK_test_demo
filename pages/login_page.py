from pages.base_page import BasePage
from locators.login_locators import LoginPageLocators


class LoginPage(BasePage):

    def authorization(self, login, password):
        # Авторизация
        self.visibility_of_element_located(*LoginPageLocators.LOGIN_LINK)
        input_login = self.find_element(*LoginPageLocators.LOGIN_LINK)
        input_password = self.find_element(*LoginPageLocators.PASSWORD_LINK)
        button_login = self.find_element(*LoginPageLocators.BUTTON_LOGIN)
        input_login.send_keys(login)
        input_password.send_keys(password)
        button_login.click()

