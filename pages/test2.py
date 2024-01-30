import json
import time
from datetime import datetime
import os
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.preparation_transaction_locators import PreparationTransactionLocators


class ParsDataPreparationTransaction:

    def __init__(self):
        self.file_data_preparation_transaction_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'data', 'data_preparation_transaction.json'))

    def read_data_preparation_transaction(self):
        with open(self.file_data_preparation_transaction_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            id_card = data['id_card']
            current_index = data['current_index']

            return {'id_card': id_card, 'current_index': current_index}

    def save_data_preparation_transaction(self, data):
        with open(self.file_data_preparation_transaction_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)


class PreparationTransaction(BasePage):

    def click_client_agrees(self):
        self.invisibility_of_element_located(*PreparationTransactionLocators.REQUISITES_BOX)
        self.element_is_clickable(*PreparationTransactionLocators.CLIENT_AGREES)
        client_agrees = self.find_element(*PreparationTransactionLocators.CLIENT_AGREES)
        client_agrees.click()

    def fill_id_card(self):
        input_id_card = self.find_element(*PreparationTransactionLocators.ID_CARD)
        get_card_status = self.find_element(*PreparationTransactionLocators.GET_CARD_STATUS)

        data_preparation_transaction = ParsDataPreparationTransaction()
        data_preparation_transaction_read = data_preparation_transaction.read_data_preparation_transaction()
        data_preparation_transaction_save = data_preparation_transaction.save_data_preparation_transaction()



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

        data_preparation_transaction_save(data_preparation_transaction)





