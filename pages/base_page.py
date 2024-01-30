import time
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from locators.basa_page_locators import BasePageLocators


class BasePage(object):

    def __init__(self, driver=None, url=None, timeout=20):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def find_element(self, how, what):
        return self.driver.find_element(how, what)

    def element_is_clickable(self, how, what, timeout=10):
        try:
            wait(self.driver, timeout).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    def element_is_not_clickable(self, how, what, timeout=10):
        try:
            wait(self.driver, timeout).until_not(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    def visibility_of_element_located(self, how, what, timeout=20):
        try:
            wait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def invisibility_of_element_located(self, how, what, timeout=20):
        try:
            wait(self.driver, timeout).until(EC.invisibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def presence_of_element_located(self, how, what, timeout=20):
        try:
            wait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def staleness_of(self, how, what, timeout=20):
        try:
            wait(self.driver, timeout).until(EC.staleness_of(how, what))
        except TimeoutException:
            return False
        return True

    def close_new_window(self):
        main_window_handle = self.driver.current_window_handle
        wait(self.driver, 15).until(lambda driver: len(driver.window_handles) > 1)  # Ожидание открытия нового окна
        windows = self.driver.window_handles  # Поиск всех окон
        self.driver.switch_to.window(windows[-1])  # Переключение на последнее из тех, что открылось
        self.driver.close()  # Закрытие окна
        self.driver.switch_to.window(main_window_handle)  # переключение на основное окно

    def go_task_list(self):
        self.element_is_clickable(*BasePageLocators.TASK_LIST)
        task_list = self.driver.find_element(*BasePageLocators.TASK_LIST)
        task_list.click()

    def go_application_list(self):
        self.visibility_of_element_located(*BasePageLocators.APPLICATION_LIST, timeout=30)
        self.element_is_clickable(*BasePageLocators.APPLICATION_LIST, timeout=30)
        application_list = self.driver.find_element(*BasePageLocators.APPLICATION_LIST)
        application_list.click()





