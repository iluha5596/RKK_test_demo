from selenium.webdriver.common.by import By


class MyApplicationsLocators:
    BUTTON_SEARCH_PARAMETERS = (By.XPATH, '//button[@field-code="isShowParameters"]')
    INPUT_NUMBER_REQ = (By.XPATH, '//input[@field-code="INPUT_NUMBER_REQ"]')
    BUTTON_APPLY = (By.XPATH, '//span[text()="Применить"]')

