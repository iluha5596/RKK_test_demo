import os
from locators.short_form_locators import ShortFormLocators
from pages.base_page import BasePage
import json


def read_data_short_form():
    file_short_form_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'data', 'data_short_form.json'))
    with open(file_short_form_path, 'r') as file:
        data_short_form = json.load(file)

    amount_credit = data_short_form['amount_credit']
    monthly_income_amount = data_short_form['monthly_income_amount']

    return {'amount_credit': amount_credit, 'monthly_income_amount': monthly_income_amount}


def path_document_download():
    file_short_form_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'data', 'document_download.jpg'))
    return file_short_form_path


class ShortFormPage(BasePage):

    def fill_required_fields_short_form(self, driver):
        # Заполнить обязательные поля и отправить заявку далее по процессу
        self.filling_short_form()
        self.generate_documents()
        self.modal_window_generate_documents()
        base_page = BasePage(driver)
        base_page.close_new_window()
        self.attach_client_consent_file()
        self.next_form()

    def filling_short_form(self):
        # Заполнить обязательные поля
        input_amount_credit = self.driver.find_element(*ShortFormLocators.INPUT_AMOUNT_CREDIT)
        input_monthly_income_amount = self.driver.find_element(*ShortFormLocators.INPUT_MONTHLY_INCOME_AMOUNT)
        button_file_passport = self.driver.find_element(*ShortFormLocators.BUTTON_FILE_PASSPORT_DOWNLOAD)
        button_file_photo = self.driver.find_element(*ShortFormLocators.BUTTON_FILE_PHOTO_DOWNLOAD)

        data_short_form = read_data_short_form()
        input_amount_credit.send_keys(data_short_form['amount_credit'])
        input_monthly_income_amount.send_keys(data_short_form['monthly_income_amount'])

        document_download = path_document_download()
        button_file_passport.send_keys(document_download)
        button_file_photo.send_keys(document_download)

    def generate_documents(self):
        # Нажать на "Сформировать документы"
        self.element_is_clickable(*ShortFormLocators.BUTTON_FILE_PASSPORT_UNLOAD)
        self.element_is_clickable(*ShortFormLocators.BUTTON_FILE_PHOTO_UNLOAD)
        self.element_is_clickable(*ShortFormLocators.BUTTON_GENERATE_DOCUMENTS)
        button_generate_documents = self.driver.find_element(*ShortFormLocators.BUTTON_GENERATE_DOCUMENTS)
        self.driver.execute_script('arguments[0].click();', button_generate_documents)

    def modal_window_generate_documents(self):
        # Нажать на "Сформировать документы и отправить на печать"
        self.element_is_clickable(*ShortFormLocators.BUTTON_GENERATE_DOCUMENTS_SEND_PRINT)
        button_generate_documents_send_print = self.driver.find_element(
            *ShortFormLocators.BUTTON_GENERATE_DOCUMENTS_SEND_PRINT)
        button_generate_documents_send_print.click()

    def attach_client_consent_file(self):
        # Вложить файл в Согласие клиента
        document_download = path_document_download()
        self.element_is_clickable(*ShortFormLocators.BUTTON_FILE_CONSENT_DOWNLOAD)
        button_file_consent = self.driver.find_element(*ShortFormLocators.BUTTON_FILE_CONSENT_DOWNLOAD)
        button_file_consent.send_keys(document_download)

    def determine_application_number(self):
        # Возращает номер заявки
        self.visibility_of_element_located(*ShortFormLocators.APPLICATION_NUMBER)
        number_app = (self.driver.find_element(*ShortFormLocators.APPLICATION_NUMBER)).text
        print(number_app)
        return number_app

    def next_form(self):
        # Отправить заявку далее по процессу
        self.element_is_clickable(*ShortFormLocators.BUTTON_FILE_CONSENT_UNLOAD)
        button_go_full_form = self.driver.find_element(*ShortFormLocators.BUTTON_NEXT_FORM)
        button_go_full_form.click()
