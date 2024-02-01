from selenium.webdriver.common.by import By


class SignAgreementClientLocators:
    GENERATE_DOCUMENTS = (By.XPATH, '//button[@field-code="generate_btn"]')
    GENERATE_DOCUMENTS_AND_PRINT = (By.XPATH, '//button[@field-code="button_y2rMCaP9"]')
    DOCUMENTS = (By.XPATH, '//tr[@class="p-datatable-row"]')
    INPUT_DOCUMENTS = (By.XPATH, '//input[@type="file"]')
    REMOVE_EVERYTHING = (By.XPATH, '//span[text()="Снять все"]')
    DOCUMENT_CHECKBOX = (By.XPATH, '(//div[@class="p-checkbox-box p-component"])[1]')
    LOAN_AGREEMENT_SIGNED = (By.XPATH, '//label[text()="Кредитный договор подписан"]/..//span[@class="p-radiobutton-icon p-c"]')
    ADDED_DOCUMENTS = (By.XPATH, '//div[@class="p-buttonset"]')
    BUTTON_NEXT = (By.XPATH, '//button[@field-code="button_tPyELAEv"]')