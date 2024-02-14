import os
import allure
from locators.short_form_locators import ShortFormLocators
from pages.base_page import BasePage
from data.read_data import ShortFormData
from data.document_download import DocumentDownload


def document():
    document_download = os.path.abspath('../data/document_download.jpg')
    return document_download


class ShortFormPage(BasePage):
    application_id = None

    def fill_required_fields_short_form(self, driver):
        # Заполнить обязательные поля и отправить заявку далее по процессу
        with allure.step('Заполнение обязательных полей на короткой форме'):
            self.filling_short_form()
            self.generate_documents()
            self.modal_window_generate_documents()
            base_page = BasePage(driver)
            base_page.close_new_window()
            self.attach_client_consent_file()
        with allure.step('Отправить заявку далее по процссу с короткой анкеты'):
            self.next_form()

    def filling_short_form(self):
        # Заполнение обязательных полей
        short_form_data = ShortFormData('../data/data_short_form.json')
        input_amount_credit = self.find_element(*ShortFormLocators.INPUT_AMOUNT_CREDIT)
        input_monthly_income_amount = self.find_element(*ShortFormLocators.INPUT_MONTHLY_INCOME_AMOUNT)
        button_file_passport = self.find_element(*ShortFormLocators.BUTTON_FILE_PASSPORT_DOWNLOAD)
        button_file_photo = self.find_element(*ShortFormLocators.BUTTON_FILE_PHOTO_DOWNLOAD)

        input_amount_credit.send_keys(short_form_data.amount_credit)
        input_monthly_income_amount.send_keys(short_form_data.monthly_income_amount)

        document_download = DocumentDownload('../data/document_download.jpg')
        button_file_passport.send_keys(document_download.document_download)
        button_file_photo.send_keys(document_download.document_download)

    def generate_documents(self):
        # Нажать на "Сформировать документы"
        self.element_is_clickable(*ShortFormLocators.BUTTON_FILE_PASSPORT_UNLOAD)
        self.element_is_clickable(*ShortFormLocators.BUTTON_FILE_PHOTO_UNLOAD)
        self.element_is_clickable(*ShortFormLocators.BUTTON_GENERATE_DOCUMENTS)
        button_generate_documents = self.find_element(*ShortFormLocators.BUTTON_GENERATE_DOCUMENTS)
        self.driver.execute_script('arguments[0].click();', button_generate_documents)

    def modal_window_generate_documents(self):
        # Нажать на "Сформировать документы и отправить на печать"
        self.element_is_clickable(*ShortFormLocators.BUTTON_GENERATE_DOCUMENTS_SEND_PRINT)
        button_generate_documents_send_print = self.find_element(
            *ShortFormLocators.BUTTON_GENERATE_DOCUMENTS_SEND_PRINT)
        button_generate_documents_send_print.click()

    def attach_client_consent_file(self):
        # Вложить файл в Согласие клиента
        document_download = DocumentDownload('../data/document_download.jpg')
        self.element_is_clickable(*ShortFormLocators.BUTTON_FILE_CONSENT_DOWNLOAD)
        button_file_consent = self.find_element(*ShortFormLocators.BUTTON_FILE_CONSENT_DOWNLOAD)
        button_file_consent.send_keys(document_download.document_download)

    def determine_application_number(self):
        # Возращает номер заявки
        self.visibility_of_element_located(*ShortFormLocators.APPLICATION_NUMBER)
        number_app = (self.find_element(*ShortFormLocators.APPLICATION_NUMBER)).text
        ShortFormPage.application_id = number_app
        print(number_app)

    def next_form(self):
        # Отправить заявку далее по процессу
        self.element_is_clickable(*ShortFormLocators.BUTTON_FILE_CONSENT_UNLOAD)
        button_go_full_form = self.find_element(*ShortFormLocators.BUTTON_NEXT_FORM)
        button_go_full_form.click()
