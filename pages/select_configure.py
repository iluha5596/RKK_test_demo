import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.select_configure_locators import SelectConfigureLocators


class SelectConfigure(BasePage):

    def choose_tariff_passage_task(self, tariff):
        # Выбрать тариф и отправить заявку далее по процессу
        with allure.step('Проход заявки на задачу "Выбрать и сконфигурировать продукт"'):
            with allure.step('Выбрать тариф'):
                self.choose_tariff(tariff)
            with allure.step('Выбрать действие "Переход на принятие решения" '
                             'и отправить заявку далее по процессу с задачи "Выбрать и сконфигурировать"'):
                self.choose_transition_decision_making()
                self.select_configure_next_form()

    def choose_tariff(self, tariff):
        # Выбрать тариф
        tariff_locator = SelectConfigureLocators.TARIFF[1].format(tariff)
        self.element_is_clickable(By.XPATH, tariff_locator, timeout=60)
        privilege_credit_card_installment = self.find_element(By.XPATH, tariff_locator)
        self.driver.execute_script('arguments[0].click();', privilege_credit_card_installment)

    def choose_transition_decision_making(self):
        # Выбрать действие "Переход на принятие решения"
        self.element_is_clickable(*SelectConfigureLocators.TRANSITION_DECISION_MAKING, timeout=120)
        transition_decision_making = self.find_element(*SelectConfigureLocators.TRANSITION_DECISION_MAKING)
        self.driver.execute_script('arguments[0].click();', transition_decision_making)

    def select_configure_next_form(self):
        # Нажать "Далее"
        self.element_is_clickable(*SelectConfigureLocators.BUTTON_NEXT)
        button_next = self.find_element(*SelectConfigureLocators.BUTTON_NEXT)
        button_next.click()
        self.element_is_not_clickable(*SelectConfigureLocators.BUTTON_NEXT, timeout=60)

