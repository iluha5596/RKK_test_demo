from selenium.webdriver.common.by import By


class NotifyClientLocators:
    CLIENT_AGREES = (
    By.XPATH, '//*[text()="Клиент согласен (находится в офисе выдачи кредита с необходимыми документами)"]'
              '/..//div[@class="p-radiobutton-box p-component"]')
    BUTTON_NEXT = (By.XPATH, '//span[text()="Далее"]')
