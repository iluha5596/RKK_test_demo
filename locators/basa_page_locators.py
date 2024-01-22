from selenium.webdriver.common.by import By


class BasePageLocators:
    TASK_LIST = (By.XPATH, '//span[text()="Задачи"]')
    APPLICATION_LINK_NUMBER = (By.XPATH, '//a[text()="{}"]')
    APPLICATION_LIST = (By.XPATH, '//span[text()="Заявки"]')
