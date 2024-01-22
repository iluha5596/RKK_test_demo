from pages.base_page import BasePage
from locators.application_locators import ApplicationLocators
from selenium.common.exceptions import NoSuchElementException


class Application(BasePage):
    def go_task(self):
        self.element_is_clickable(*ApplicationLocators.BUTTON_TAKE_JOB)
        button_take_job = self.driver.find_element(*ApplicationLocators.BUTTON_TAKE_JOB)
        button_take_job.click()

    def expectation_task(self):
        while True:
            if self.element_is_clickable(*ApplicationLocators.BUTTON_TAKE_JOB, timeout=3):
                break
            else:
                self.driver.refresh()

    def check_hire_no_form(self):
        # После завершения задачи проверить, что в заявке нет "Взять в работу" завершённую задачу
        if self.presence_of_element_located(*ApplicationLocators.CURRENT_TASK, timeout=2):
            self.driver.refresh()





