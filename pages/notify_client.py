from pages.base_page import BasePage
from locators.notify_client_locators import NotifyClientLocators


class NotifyClient(BasePage):

    def choose_client_agrees(self):
        self.element_is_clickable(*NotifyClientLocators.CLIENT_AGREES, timeout=60)
        client_agrees = self.driver.find_element(*NotifyClientLocators.CLIENT_AGREES)
        self.driver.execute_script('arguments[0].click();', client_agrees)

    def notify_client_next_form(self):
        self.element_is_clickable(*NotifyClientLocators.BUTTON_NEXT)
        button_next = self.driver.find_element(*NotifyClientLocators.BUTTON_NEXT)
        button_next.click()
        self.element_is_not_clickable(*NotifyClientLocators.BUTTON_NEXT, timeout=5)

