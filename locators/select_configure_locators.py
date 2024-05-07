from selenium.webdriver.common.by import By


class SelectConfigureLocators:
    TARIFF = (By.XPATH, '//*[text()="{}"]/..//div[@field-code="radio-0"]')
    TRANSITION_DECISION_MAKING = (
    By.XPATH, '//*[text()="Переход на принятие решения"]/..//div[@class="p-radiobutton-box p-component"]')
    BUTTON_NEXT = (By.XPATH, '//*[@field-code="button_bPBZV9Y1"]')
