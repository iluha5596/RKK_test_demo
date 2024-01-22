import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.my_applications import MyApplicationsLocators
from locators.basa_page_locators import BasePageLocators


class ApplicationList(BasePage):

    def go_application(self, number_app):

        self.element_is_clickable(*MyApplicationsLocators.BUTTON_SEARCH_PARAMETERS)
        while True:
            if self.element_is_not_clickable(*MyApplicationsLocators.BUTTON_APPLY, timeout=1):
                button_search_parameters = self.driver.find_element(*MyApplicationsLocators.BUTTON_SEARCH_PARAMETERS)
                button_search_parameters.click()
                time.sleep(1)
            else:
                break

        input_number_req = self.driver.find_element(*MyApplicationsLocators.INPUT_NUMBER_REQ)
        button_apply = self.driver.find_element(*MyApplicationsLocators.BUTTON_APPLY)
        input_number_req.send_keys(number_app)
        button_apply.click()
        application_link_locator = BasePageLocators.APPLICATION_LINK_NUMBER[1].format(number_app)
        application_link = self.driver.find_element(By.XPATH, application_link_locator)
        application_link.click()

    def search_application(self, number_app):
        application_link_locator = BasePageLocators.APPLICATION_LINK_NUMBER[1].format(number_app)
        self.element_is_clickable(By.XPATH, application_link_locator)
        application_link = self.driver.find_element(By.XPATH, application_link_locator)
        application_link.click()


