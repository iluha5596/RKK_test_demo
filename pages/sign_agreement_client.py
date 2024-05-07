import allure
from data.document_download import DocumentDownload
from pages.base_page import BasePage
from locators.sign_agreement_client_locators import SignAgreementClientLocators
from selenium.webdriver.support.ui import WebDriverWait as wait


class SignAgreementClient(BasePage):
    count_window = 1

    def fill_sign_agreement_client(self, driver):
        # Вложить все документы и отправить заявку далее по процессу
        with allure.step('Задача "Подписание"'):
            with allure.step('Вложить все документы'):
                base_page = BasePage(driver)
                self.click_generate_documents()
                self.count_documents_print()
                self.click_generate_documents_and_print()
                self.number_of_windows_to_be(SignAgreementClient.count_window)
                base_page.switching_main_window()
                self.add_documents()
            with allure.step('Выбрать действие "Кредитный договор подписан" и отправить заявку на выдачу'):
                self.choose_loan_agreement_signed()
                self.sign_agreement_client_next()

    def click_generate_documents(self):
        # Кликнуть на "Сформировать документы"
        self.element_is_clickable(*SignAgreementClientLocators.GENERATE_DOCUMENTS)
        generate_documents = self.find_element(*SignAgreementClientLocators.GENERATE_DOCUMENTS)
        generate_documents.click()

    def count_documents_print(self):
        self.visibility_of_element_located(*SignAgreementClientLocators.DOCUMENTS)
        element_documents = self.find_elements(*SignAgreementClientLocators.DOCUMENTS)
        count_document = len(element_documents)
        SignAgreementClient.count_window += count_document

    def click_generate_documents_and_print(self):
        # Кликнуть на "Сформировать документы и отправить на печать"
        self.visibility_of_element_located(*SignAgreementClientLocators.GENERATE_DOCUMENTS_AND_PRINT)
        self.element_is_clickable(*SignAgreementClientLocators.GENERATE_DOCUMENTS_AND_PRINT)
        generate_documents_and_print = self.find_element(*SignAgreementClientLocators.GENERATE_DOCUMENTS_AND_PRINT)
        generate_documents_and_print.click()

    def add_documents(self):
        # Добавить документы
        document_download = DocumentDownload('data/document_download.jpg')
        input_documents = self.find_elements(*SignAgreementClientLocators.INPUT_DOCUMENTS)
        for document in input_documents:
            document.send_keys(document_download.document_download)

    def choose_loan_agreement_signed(self):
        # Выбрать действие "Кредитный договор подписан"
        self.element_is_clickable(*SignAgreementClientLocators.LOAN_AGREEMENT_SIGNED)
        loan_agreement_signed = self.find_element(*SignAgreementClientLocators.LOAN_AGREEMENT_SIGNED)
        wait(self.driver, 15).until(lambda _:
                                    len(self.find_elements(*SignAgreementClientLocators.ADDED_DOCUMENTS)) - 1 >=
                                    len(self.find_elements(*SignAgreementClientLocators.INPUT_DOCUMENTS)))
        loan_agreement_signed.click()

    def sign_agreement_client_next(self):
        # Нажать "Далее"
        self.element_is_clickable(*SignAgreementClientLocators.BUTTON_NEXT)
        button_next = self.find_element(*SignAgreementClientLocators.BUTTON_NEXT)
        button_next.click()
