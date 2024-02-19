from selenium.webdriver.common.by import By


class FullFormLocators:
    # Запрашиваемые условия
    CREDIT_TERM = (By.XPATH, '//div[@class=" p-col-6 required"]/input[@class="p-inputtext p-component"]')
    PURPOSE_CREDIT = (By.XPATH, '//div[@field-code="purpose"]')
    PURPOSE_CREDIT_CAR = (By.XPATH, '//li[@aria-label="Покупка автомобиля"]')
    # Инофрмация по клиенту
    FAMILY_STATUS = (By.XPATH, '//div[@field-code="marriageStatus"]')
    FAMILY_STATUS_NEVER_MARRIED = (By.XPATH, '//li[@aria-label="В браке не был(а)"]')
    COUNT_CHILDREN = (By.XPATH, '//input[@field-code="childrenCount"]')
    DEPENDS_COUNT = (By.XPATH, '//input[@field-code="dependsCount"]')
    CORRESPONDENCE = (By.XPATH, '//label[@title="Прошу направлять мне корреспонденцию по адресу"]')
    # Телефон контактного лица
    PHONE_CONTACT_PERSON = (By.XPATH, '//*[text()="Телефон контактного лица"]/../../..//*[@field-code="PHONE_CONTROL"]')
    # Адреса
    REASONS_RESIDENCE = (By.XPATH, '//div[@field-code="residenceReason"]')
    BASIS_RESIDENCE_OWN = (By.XPATH, '//li[@aria-label="Собственность"]')
    # Доходы
    SOURCE_INCOME = (By.XPATH, '//div[@field-code="incomeSource"]')
    SOURCE_INCOME_EMPLOYMENT = (By.XPATH, '//li[@aria-label="Работа по найму"]')
    EMPLOYER_NAME = (By.XPATH, '//input[@field-code="empl_search"]')
    ORGANIZATION_FROM_LIST = (By.XPATH, '(//li[@class="p-autocomplete-list-item"])[1]')
    YEARS_EXPERIENCE = (By.XPATH, '//input[@field-code="seniorityYear"]')
    MONTHS_EXPERIENCE = (By.XPATH, '//input[@field-code="seniorityMonth"]')
    POSITION = (By.XPATH, '//input[@field-code="position"]')
    POSITION_LEVEL = (By.XPATH, '//div[@field-code="positionType"]')
    POSITION_LEVEL_TOP_MANAGER = (By.XPATH, '//li[@aria-label="Топ-менеджер"]')
    COPY_FROM_LEGAL_ADDRESS = (By.XPATH, '//span[text()="Скопировать из юридического адреса"]')
    PHONE_TYPE = (By.XPATH, '//div[@field-code="phoneType"]')
    CLIENT_WORK_PHONE = (By.XPATH, '//li[@aria-label="Рабочий телефон клиента"]')
    EMPLOYER_PHONE = (By.XPATH, '//*[text()="Телефоны работодателя"]/../../../..//*[@field-code="PHONE_CONTROL"]')
    MESSAGE_ADDING_PHONE = (By.XPATH, '//span[text()="Телефоны работодателя"]/../../..//*[starts-with(text(), "Оператор связи")]')
    EMPLOYER_ADDRESS = (By.XPATH, '//span[text()="Фактический адрес работодателя"]/../../..//*[@field-code="address_search1"]')
    INN = (By.XPATH, '(//input[@class="p-inputtext p-component p-autocomplete-input"])[2]')
    # Далее
    FULL_APP_NEXT_BTN = (By.XPATH, '//span[text()="Далее"]')

