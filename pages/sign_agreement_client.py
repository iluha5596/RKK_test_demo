import os
from pages.base_page import BasePage
from locators.sign_agreement_client_locators import  SignAgreementClientLocators
from selenium.webdriver.support.ui import WebDriverWait as wait


def path_document_download():
    file_short_form_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'data', 'document_download.jpg'))
    return file_short_form_path


class SignAgreementClient(BasePage):

    def click_generate_documents(self):
        self.element_is_clickable(*SignAgreementClientLocators.GENERATE_DOCUMENTS)
        generate_documents = self.find_element(*SignAgreementClientLocators.GENERATE_DOCUMENTS)
        generate_documents.click()

    def click_generate_documents_and_print(self):
        self.visibility_of_element_located(*SignAgreementClientLocators.GENERATE_DOCUMENTS_AND_PRINT)
        self.element_is_clickable(*SignAgreementClientLocators.GENERATE_DOCUMENTS_AND_PRINT)
        generate_documents_and_print = self.find_element(*SignAgreementClientLocators.GENERATE_DOCUMENTS_AND_PRINT)
        generate_documents_and_print.click()

    def add_documents(self):
        document_download = path_document_download()
        input_documents = self.find_elements(*SignAgreementClientLocators.INPUT_DOCUMENTS)
        for document in input_documents:
            document.send_keys(document_download)

    def choose_loan_agreement_signed(self):
        self.element_is_clickable(*SignAgreementClientLocators.LOAN_AGREEMENT_SIGNED)
        loan_agreement_signed = self.find_element(*SignAgreementClientLocators.LOAN_AGREEMENT_SIGNED)
        wait(self.driver, 15).until(lambda _:
                                    len(self.find_elements(*SignAgreementClientLocators.ADDED_DOCUMENTS)) - 1 >= len(self.find_elements(*SignAgreementClientLocators.INPUT_DOCUMENTS)))
        print(f'OK. Количество добавленных документов: {len(self.find_elements(*SignAgreementClientLocators.ADDED_DOCUMENTS))}, количество инпутов для документов: {len(self.find_elements(*SignAgreementClientLocators.INPUT_DOCUMENTS))}')
        loan_agreement_signed.click()

    def sign_agreement_client_next(self):
        self.element_is_clickable(*SignAgreementClientLocators.BUTTON_NEXT)
        button_next = self.find_element(*SignAgreementClientLocators.BUTTON_NEXT)
        button_next.click()



