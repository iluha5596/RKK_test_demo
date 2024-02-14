import allure
from pages.base_page import BasePage
from locators.notify_client_locators import NotifyClientLocators


class NotifyClient(BasePage):

    def notify_client_passage_task(self):
        # Отправить заявку далее по процессу
        with allure.step('Выбрать действие "Клиент согласен..." '
                         'и отправить заявку далее по процессу с задачи "Уведомить клиента"'):
            self.choose_client_agrees()
            self.notify_client_next_form()

    def choose_client_agrees(self):
        # Выбрать действие "Клиент согласен..."
        self.element_is_clickable(*NotifyClientLocators.CLIENT_AGREES, timeout=60)
        client_agrees = self.find_element(*NotifyClientLocators.CLIENT_AGREES)
        self.driver.execute_script('arguments[0].click();', client_agrees)

    def notify_client_next_form(self):
        # Нажать кнопку Далее
        self.element_is_clickable(*NotifyClientLocators.BUTTON_NEXT)
        button_next = self.find_element(*NotifyClientLocators.BUTTON_NEXT)
        button_next.click()
        self.element_is_not_clickable(*NotifyClientLocators.BUTTON_NEXT, timeout=60)

