from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
from locators.basa_page_locators import BasePageLocators


class BasePage(object):

    def __init__(self, driver=None, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def find_element(self, how, what):
        return self.driver.find_element(how, what)

    def find_elements(self, how, what):
        return self.driver.find_elements(how, what)

    def not_empty_value(self, element, timeout=30):
        return wait(self.driver, timeout).until(lambda x: element.get_attribute('value') != '')

    def number_of_windows_to_be(self, count_window, timeout=30):
        try:
            wait(self.driver, timeout).until(EC.number_of_windows_to_be(count_window))
        except TimeoutException:
            return False
        return True

    def element_is_clickable(self, how, what, timeout=30):
        try:
            wait(self.driver, timeout).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    def element_is_not_clickable(self, how, what, timeout=30):
        try:
            wait(self.driver, timeout).until_not(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    def visibility_of_element_located(self, how, what, timeout=30):
        try:
            wait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def invisibility_of_element_located(self, how, what, timeout=30):
        try:
            wait(self.driver, timeout).until(EC.invisibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def presence_of_element_located(self, how, what, timeout=30):
        try:
            wait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
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

    def close_new_windows(self):
        # Получаем текущее количество окон
        main_window_handle = self.driver.current_window_handle
        # Получаем все окна
        all_windows = self.driver.window_handles
        # Закрываем новые окна и переключаемся обратно на основное окно
        for window in all_windows:
            try:
                self.driver.switch_to.window(window)
                self.driver.close()
            except NoSuchWindowException:
                # Пропускаем закрытое окно и переходим к следующему
                continue
        # Переключаемся обратно на основное окно
        self.driver.switch_to.window(main_window_handle)

    def switching_main_window(self):
        main_window_handle = self.driver.current_window_handle
        self.driver.switch_to.window(main_window_handle)

    def go_task_list(self):
        self.element_is_clickable(*BasePageLocators.TASK_LIST)
        task_list = self.find_element(*BasePageLocators.TASK_LIST)
        task_list.click()

    def go_application_list(self):
        # Переход на вкладку список заявок
        self.element_is_clickable(*BasePageLocators.APPLICATION_LIST, timeout=180)
        application_list = self.find_element(*BasePageLocators.APPLICATION_LIST)
        application_list.click()

    def application_search(self, number_app):
        self.go_application_list()
        # Поиск заявки
        application_link_locator = BasePageLocators.APPLICATION_LINK_NUMBER[1].format(number_app)
        self.element_is_clickable(By.XPATH, application_link_locator)
        application_link = self.find_element(By.XPATH, application_link_locator)
        application_link.click()





