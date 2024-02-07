import time
import pytest
from pages.login_page import LoginPage
from decouple import config
from pages.application import Application
from pages.application_list import ApplicationList
from pages.short_form import ShortFormPage
from pages.base_page import BasePage
from pages.full_form import FullForm
from pages.select_configure import SelectConfigure
from pages.notify_client import NotifyClient
from pages.preparation_transaction import PreparationTransaction
from pages.sign_agreement_client import SignAgreementClient
from db.assert_db import AssertDB
from pages.my_task import MyTask

application_id = None

class PassTask:

    def fill_required_fields_short_form(self, driver):
        # Заполнение обязательных полей на задаче Короткая анкета
        short_form_page = ShortFormPage(driver)
        self.number_app = short_form_page.determine_application_number()
        global application_id
        application_id = self.number_app
        short_form_page.filling_short_form()
        short_form_page.generate_documents()
        short_form_page.modal_window_generate_documents()
        base_page = BasePage(driver)
        base_page.close_new_window()
        short_form_page.attach_client_consent_file()
        short_form_page.next_form()
        print(application_id)

    def fill_required_fields_full_form(self, driver):
        # Заполнение обязательных полей на полной форме
        full_form = FullForm(driver)
        full_form.filling_required_fields_full_form()
        full_form.full_app_next_form()

    def select_tariff_cc(self, driver, tariff):
        # Выбор тарифа и отправка заявки далее по процессу
        select_configure_page = SelectConfigure(driver)
        select_configure_page.choose_tariff(tariff=tariff)
        select_configure_page.choose_transition_decision_making()
        select_configure_page.select_configure_next_form()

    def notify_client_next_form(self, driver):
        # Отправить заявку далее по процессу с Уведомить клиента
        notify_client_page = NotifyClient(driver)
        notify_client_page.choose_client_agrees()
        notify_client_page.notify_client_next_form()

    def application_search(self, driver):
        # Переход на вкладку список заявок
        base_page = BasePage(driver)
        base_page.go_application_list()
        # Поиск заявки
        application_list_page = ApplicationList(driver)
        number_app = application_id
        application_list_page.search_application(number_app=number_app)

    def take_on_job_task(self, driver):
        # Взять в работу задачу
        application_page = Application(driver)
        application_page.check_hire_no_form()
        application_page.expectation_task()
        application_page.go_task()

    def passage_preparation_transaction(self, driver, tariff=None):
        # Проход до задачи Подготовка к сделке
        self.fill_required_fields_short_form(driver)
        self.application_search(driver)
        self.take_on_job_task(driver)
        self.fill_required_fields_full_form(driver)
        self.application_search(driver)
        self.take_on_job_task(driver)
        self.select_tariff_cc(driver, tariff=tariff)
        self.application_search(driver)
        self.take_on_job_task(driver)
        self.notify_client_next_form(driver)
        self.application_search(driver)
        self.take_on_job_task(driver)

    def fill_preparation_transaction_cc(self, driver):
        # Заполнение задачи Подготовка к сделке для тарифа с рассрочкой и двумя коробками
        preparation_transaction_page = PreparationTransaction(driver)
        preparation_transaction_page.go_product()
        preparation_transaction_page.on_box()
        preparation_transaction_page.add_box_solutions()
        preparation_transaction_page.click_requisites_box()
        preparation_transaction_page.filling_details_box_1()
        preparation_transaction_page.filling_details_box_2()
        preparation_transaction_page.accept_change_box()
        preparation_transaction_page.click_client_agrees()
        preparation_transaction_page.fill_id_card()
        preparation_transaction_page.enter_code_word()
        preparation_transaction_page.preparation_transaction_next_form()

    def fill_sign_agreement_client(self, driver):
        self.application_search(driver)
        self.take_on_job_task(driver)
        sign_agreement_client_page = SignAgreementClient(driver)
        base_page = BasePage(driver)
        sign_agreement_client_page.click_generate_documents()
        sign_agreement_client_page.click_generate_documents_and_print()
        base_page.close_new_windows()
        sign_agreement_client_page.add_documents()
        sign_agreement_client_page.choose_loan_agreement_signed()
        sign_agreement_client_page.sign_agreement_client_next()
        time.sleep(20)


class TestCFTMethod:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver, base_url, path):
        base_url = base_url
        path = path
        url = f'{base_url[0]}{path}'
        login_page = LoginPage(driver, url)
        login_page.open()
        # Авторизация
        login = config('LOGIN_CM_25')
        password = config('PASSWORD_CM_25')
        login_page.authorization(login=login, password=password)

    # @pytest.fixture(scope="function", autouse=True)
    # def setup(self, driver, base_url, path):
    #     base_url = base_url
    #     path = path
    #     url = f'{base_url[0]}{path}'
    #     login_page = LoginPage(driver, url)
    #     login_page.open()
    #     # Авторизация
    #     login = config('LOGIN_CM_25')
    #     password = config('PASSWORD_CM_25')
    #     login_page.authorization(login=login, password=password)
    #     number_app = 'П_00111290'
    #     # Поиск задачи через Мои задачи
    #     my_task_page = MyTask(driver)
    #     my_task_page.go_task(number_app=number_app)

    def test_tariff_installment_and_2box(self, driver, base_url):
        passage_preparation_transaction = PassTask()
        assert_db = AssertDB()
        base_url = base_url
        passage_preparation_transaction.passage_preparation_transaction(driver=driver,
                                                                        tariff='«Кредитная «Карта Привилегий» (Рассрочка)')
        passage_preparation_transaction.fill_preparation_transaction_cc(driver=driver)
        passage_preparation_transaction.fill_sign_agreement_client(driver=driver)
        assert_db.assert_db_for_tariff_installment_and_2box(base_url=base_url, application_id=application_id)

    # def test_preparation_transaction_cc(self, driver):
    #     preparation_transaction_cc_fill = PassTask()
    #     preparation_transaction_cc_fill.fill_sign_agreement_client(driver=driver)
    #     time.sleep(10)








