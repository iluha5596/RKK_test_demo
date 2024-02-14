from pages.base_page import BasePage
from pages.short_form import ShortFormPage
from locators.application_locators import ApplicationLocators


class Application(BasePage):

    def take_task_through_application_form(self, driver):
        # Взять задачу в работу через "Взять в работу" в заявке
        base_page = BasePage(driver)
        short_form_page = ShortFormPage(driver)
        base_page.application_search(number_app=short_form_page.application_id)
        self.take_on_job_task()

    def take_on_job_task(self):
        # Взять в работоу задачу
        self.check_hire_no_form()
        self.expectation_task()
        self.go_task()

    def go_task(self):
        self.element_is_clickable(*ApplicationLocators.BUTTON_TAKE_JOB)
        button_take_job = self.find_element(*ApplicationLocators.BUTTON_TAKE_JOB)
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





