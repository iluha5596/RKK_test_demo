from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_LINK = (By.XPATH, '//input[@id="username"]')
    PASSWORD_LINK = (By.XPATH, '//input[@id="password"]')
    BUTTON_LOGIN = (By.XPATH, '//input[@id="kc-login"]')
