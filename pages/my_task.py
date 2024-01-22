from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.basa_page_locators import BasePageLocators


class MyTask(BasePage):

    def search_task(self, number_app):
        application_link_locator = BasePageLocators.APPLICATION_LINK_NUMBER[1].format(number_app)
        self.element_is_clickable(By.XPATH, application_link_locator)
        application_link = self.driver.find_element(By.XPATH, application_link_locator)
        application_link.click()

    def expectation_task(self, number_app):
        application_link_locator = BasePageLocators.APPLICATION_LINK_NUMBER[1].format(number_app)
        self.driver.refresh()
        while True:
            if self.element_is_not_clickable(By.XPATH, application_link_locator):
                application_link = self.driver.find_element(By.XPATH, application_link_locator)
                application_link.click()
                break
            else:
                self.driver.refresh()




