from selenium.webdriver.common.by import By


class PreparationTransactionLocators:
    PRODUCT = (By.XPATH, '//span[text()="Продукт"]')
    SERVICE_BOX = (By.XPATH, '//*[text()="Коробка КК"]/../..//span[@class="p-inputswitch-slider"]')
    TOTAL_COST_BOX = (By.XPATH, '//*[text()="Коробка КК"]/../../../../../../../../../../..//input[@field-code="amount"]')
    COUNT_BOX_SOLUTIONS = (By.XPATH, '//input[@field-code="quantity"]')
    REQUISITES_BOX = (By.XPATH, '//button[@field-code="requisites"]//span[@class="p-button-text p-c"]')
    CONTRACT_NUMBER = (By.XPATH, r'//label[@title="Номер договора \ сертификата"]/..//input[@field-code="reqContractNumber"]')
    CONTRACT_DATA = (By.XPATH, r'//label[@title="Дата договора \ сертификата"]/..//input[@field-code="reqContractDate"]')
    BOX_TWO = (By.XPATH, '//span[text()="Коробка №2"]')
    REQUISITES_BOX_ACCEPT = (By.XPATH, '//span[text()="Принять"]')
    CLIENT_AGREES = (By.XPATH, '//*[text()="Клиент согласен (печать и подписание договора, при необходимости обновление карточки клиента в ЦФТ)"]'
                               '/..//span[@class="p-radiobutton-icon p-c"]')
    ID_CARD = (By.XPATH, '//input[@field-code="cardId"]')
    ID_CARD_VALUE = (By.XPATH, '//input[@value="{}"]')
    GET_CARD_STATUS = (By.XPATH, '//span[text()="Получить статус карты"]')
    ERROR_TEXT_STATUS_CARD = (By.XPATH, '//div[@class="ErrorText"]')
    TIPE_CARD = (By.XPATH, '//label[text()="Тип выбранной карты"]')
    ENTER_CODEWORD = (By.XPATH, '//span[text()="Ввести КС"]')
    CODEWORD = (By.XPATH, '//*[text()="Введите кодовое слово"]/../..//input[@field-code="word"]')
    SAVE_CODEWORD = (By.XPATH, '//button[@field-code="button_YuxmWlpY"]//span[text()="Сохранить"]')
    BUTTON_NEXT = (By.XPATH, '//button[@field-code="buttonNext"]')