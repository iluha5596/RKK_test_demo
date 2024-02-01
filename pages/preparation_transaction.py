import json
import time
from datetime import datetime
import os
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.preparation_transaction_locators import PreparationTransactionLocators
from selenium.webdriver.common.action_chains import ActionChains


class ParsDataPreparationTransaction:

    def __init__(self):
        self.file_data_preparation_transaction_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'data', 'data_preparation_transaction.json'))

    def read_data_preparation_transaction(self):
        with open(self.file_data_preparation_transaction_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            count_box_solutions = data['count_box_solutions']
            contract_number_box_1 = data['contract_number_box_1']
            contract_number_box_2 = data['contract_number_box_2']
            codeword = data['codeword']
            id_card = data['id_card']
            current_index = data['current_index']

            return {'count_box_solutions': count_box_solutions, 'contract_number_box_1': contract_number_box_1,
                    'contract_number_box_2': contract_number_box_2, 'codeword': codeword, 'id_card': id_card,
                    'current_index': current_index}, data

    def save_data_preparation_transaction(self, data):
        with open(self.file_data_preparation_transaction_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)


class PreparationTransaction(BasePage):

    def __init__(self, driver=None, url=None, timeout=20):
        super().__init__(driver, url, timeout)
        # Получение текущей даты
        today = datetime.now()
        # Форматирование даты в строку
        self.formatted_date = today.strftime("%d.%m.%Y")

    def go_product(self):
        self.element_is_clickable(*PreparationTransactionLocators.PRODUCT, timeout=60)
        product = self.find_element(*PreparationTransactionLocators.PRODUCT)
        product.click()

    def on_box(self):
        self.element_is_clickable(*PreparationTransactionLocators.SERVICE_BOX, timeout=60)
        service_box = self.find_element(*PreparationTransactionLocators.SERVICE_BOX)
        service_box.click()

    def add_box_solutions(self):
        data_preparation_transaction = ParsDataPreparationTransaction()
        data_preparation_transaction_read, data = data_preparation_transaction.read_data_preparation_transaction()
        self.visibility_of_element_located(*PreparationTransactionLocators.COUNT_BOX_SOLUTIONS, timeout=60)
        box_solution = self.find_element(*PreparationTransactionLocators.COUNT_BOX_SOLUTIONS)
        box_solution.send_keys(data_preparation_transaction_read['count_box_solutions'])

    def click_requisites_box(self):
        self.element_is_clickable(*PreparationTransactionLocators.REQUISITES_BOX, timeout=60)
        requisites_box = self.find_element(*PreparationTransactionLocators.REQUISITES_BOX)
        requisites_box.click()

    def filling_details_box_1(self):
        data_preparation_transaction = ParsDataPreparationTransaction()
        data_preparation_transaction_read, data = data_preparation_transaction.read_data_preparation_transaction()
        # Заполнение данных по первой коробке
        self.visibility_of_element_located(*PreparationTransactionLocators.CONTRACT_NUMBER)
        contract_number = self.find_element(*PreparationTransactionLocators.CONTRACT_NUMBER)
        contract_number.send_keys(data_preparation_transaction_read['contract_number_box_1'])
        contract_data = self.find_element(*PreparationTransactionLocators.CONTRACT_DATA)
        contract_data.send_keys(self.formatted_date)

    def filling_details_box_2(self):
        data_preparation_transaction = ParsDataPreparationTransaction()
        data_preparation_transaction_read, data = data_preparation_transaction.read_data_preparation_transaction()
        # Переход во вкладку второй коробки и заполнение данных
        box_two = self.find_element(*PreparationTransactionLocators.BOX_TWO)
        box_two.click()
        self.visibility_of_element_located(*PreparationTransactionLocators.CONTRACT_NUMBER)
        # Заполнение данных по второй коробке
        contract_number = self.find_element(*PreparationTransactionLocators.CONTRACT_NUMBER)
        contract_number.send_keys(data_preparation_transaction_read['contract_number_box_2'])
        contract_data = self.find_element(*PreparationTransactionLocators.CONTRACT_DATA)
        contract_data.send_keys(self.formatted_date)

    def accept_change_box(self):
        requisites_box_accept = self.find_element(*PreparationTransactionLocators.REQUISITES_BOX_ACCEPT)
        requisites_box_accept.click()

    def click_client_agrees(self):
        self.invisibility_of_element_located(*PreparationTransactionLocators.REQUISITES_BOX)
        self.element_is_clickable(*PreparationTransactionLocators.CLIENT_AGREES)
        client_agrees = self.find_element(*PreparationTransactionLocators.CLIENT_AGREES)
        client_agrees.click()

    def fill_id_card(self):
        input_id_card = self.find_element(*PreparationTransactionLocators.ID_CARD)
        get_card_status = self.find_element(*PreparationTransactionLocators.GET_CARD_STATUS)

        data_preparation_transaction = ParsDataPreparationTransaction()
        data_preparation_transaction_read, data = data_preparation_transaction.read_data_preparation_transaction()

        while self.invisibility_of_element_located(*PreparationTransactionLocators.TIPE_CARD, timeout=5):
            current_index = data_preparation_transaction_read['current_index']
            id_card = data_preparation_transaction_read['id_card']
            fill_id_card = id_card[current_index]
            print(f'id_card= {fill_id_card}, current_index= {current_index}')
            while input_id_card.get_attribute('value'):
                input_id_card.send_keys(Keys.BACKSPACE)
            input_id_card.send_keys(fill_id_card)
            get_card_status.click()
            # Увеличиваем текущий индекс
            data_preparation_transaction_read['current_index'] += 1
        # Сохранение индекса в файл data_preparation_transaction_read
        data_preparation_transaction.save_data_preparation_transaction(data_preparation_transaction_read)

    def enter_code_word(self):
        data_preparation_transaction = ParsDataPreparationTransaction()
        data_preparation_transaction_read, data = data_preparation_transaction.read_data_preparation_transaction()
        self.element_is_clickable(*PreparationTransactionLocators.ENTER_CODEWORD)
        enter_codeword = self.find_element(*PreparationTransactionLocators.ENTER_CODEWORD)
        enter_codeword.click()
        self.visibility_of_element_located(*PreparationTransactionLocators.CODEWORD)
        codeword = self.find_element(*PreparationTransactionLocators.CODEWORD)
        codeword.send_keys(data_preparation_transaction_read['codeword'])
        self.element_is_clickable(*PreparationTransactionLocators.SAVE_CODEWORD)
        save_codeword = self.find_element(*PreparationTransactionLocators.SAVE_CODEWORD)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(save_codeword).click().perform()
        self.invisibility_of_element_located(*PreparationTransactionLocators.SAVE_CODEWORD)

    def preparation_transaction_next_form(self):
        self.element_is_clickable(*PreparationTransactionLocators.BUTTON_NEXT)
        button_next = self.find_element(*PreparationTransactionLocators.BUTTON_NEXT)
        button_next.click()
        self.element_is_not_clickable(*PreparationTransactionLocators.BUTTON_NEXT)
        # self.driver.refresh()






