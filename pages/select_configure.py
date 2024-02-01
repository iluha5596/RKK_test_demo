import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.select_configure_locators import SelectConfigureLocators


class SelectConfigure(BasePage):

    def choose_tariff(self, tariff):
        tariff_locator = SelectConfigureLocators.TARIFF[1].format(tariff)
        self.element_is_clickable(By.XPATH, tariff_locator, timeout=60)
        privilege_credit_card_installment = self.driver.find_element(By.XPATH, tariff_locator)
        self.driver.execute_script('arguments[0].click();', privilege_credit_card_installment)

    def choose_transition_decision_making(self):
        self.element_is_clickable(*SelectConfigureLocators.TRANSITION_DECISION_MAKING, timeout=120)
        transition_decision_making = self.driver.find_element(*SelectConfigureLocators.TRANSITION_DECISION_MAKING)
        self.driver.execute_script('arguments[0].click();', transition_decision_making)

    def select_configure_next_form(self):
        self.element_is_clickable(*SelectConfigureLocators.BUTTON_NEXT)
        button_next = self.driver.find_element(*SelectConfigureLocators.BUTTON_NEXT)
        button_next.click()
        self.element_is_not_clickable(*SelectConfigureLocators.BUTTON_NEXT, timeout=20)
        # self.driver.refresh()

