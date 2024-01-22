from selenium.webdriver.common.by import By


class ShortFormLocators:
    BUTTON_NEXT_FORM = (By.XPATH, '//button[@field-code="SHORT_APP_NEXT_BTN"]')
    BUTTON_GO_FULL_FORM = (By.XPATH, '//button[@field-code="SHORT_APP_TO_FULL_MODAL_BTN"]')
    INPUT_AMOUNT_CREDIT = (By.XPATH, '//*[@field-code="amount"]')
    INPUT_MONTHLY_INCOME_AMOUNT = (By.XPATH, '//*[@field-code="SUM_CONTROL"]')
    BUTTON_FILE_PASSPORT_DOWNLOAD = (By.XPATH, '(//input[@type="file"])[1]')
    BUTTON_FILE_PHOTO_DOWNLOAD = (By.XPATH, '(//input[@type="file"])[2]')
    BUTTON_GENERATE_DOCUMENTS = (By.XPATH, '(//span[text()="Сформировать документы"])[1]')
    BUTTON_GENERATE_DOCUMENTS_SEND_PRINT = (By.XPATH, '//span[text()="Сформировать документы и отправить на печать"]')
    MODAL_WINDOW = (By.XPATH, '//div[@aria-labelledby="pr_id_20_label"]')
    BUTTON_FILE_CONSENT_DOWNLOAD = (By.XPATH, '//div[@class="p-accordion-content"]//input[@type="file"]')
    BUTTON_FILE_CONSENT_UNLOAD = (By.XPATH, '//div[@class="p-accordion-content"]//div[@class="p-buttonset"]')
    BUTTON_FILE_PASSPORT_UNLOAD = (By.XPATH, '//div[@class="p-col-12  group-shadow"]//div[@class="p-buttonset"]')
    BUTTON_FILE_PHOTO_UNLOAD = (By.XPATH, '(//div[@class="p-fluid p-grid p-align-stretch "]//div[@class="p-buttonset"])[2]')
    APPLICATION_NUMBER = (By.XPATH, '//label[text()="Номер заявки:"]/../..//a')

