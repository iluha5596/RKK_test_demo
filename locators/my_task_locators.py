from selenium.webdriver.common.by import By


class MyTaskLocators:
    BUTTON_REFRESH = (By.XPATH, '//button[@field-code="refresh"]')
    APPLICATION_LINK_NUMBER = (By.XPATH, '//a[text()="{}"]')
    TASK_LINK = (By.XPATH, '(//a[text()="{}"]/../../../../../../..//a)[1]')