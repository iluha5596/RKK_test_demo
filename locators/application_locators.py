from selenium.webdriver.common.by import By


class ApplicationLocators:
    BUTTON_TAKE_JOB = (By.XPATH, '//span[text()="Взять в работу"]')
    CURRENT_TASK = (By.XPATH, '//div[text()="Текущие задачи"]/..//tr[@class="p-datatable-row"]')
