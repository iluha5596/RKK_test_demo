import pytest
from pages.login_page import LoginPage
from decouple import config
from pages.application import Application
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


class TestCFTMethod:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver, base_url, path):
        url = f'{base_url[0]}{path}'
        login_page = LoginPage(driver, url)
        login_page.open()
        # Авторизация
        login = config('LOGIN_CM_25')
        password = config('PASSWORD_CM_25')
        login_page.authorization(login=login, password=password)

    def test_tariff_installment_and_2box(self, driver, base_url):
        passage_preparation_transaction = PassTask()
        preparation_transaction = PreparationTransaction(driver)
        sign_agreement_client = SignAgreementClient(driver)
        assert_db = AssertDB()
        passage_preparation_transaction.passage_preparation_transaction(driver, tariff='«Кредитная «Карта Привилегий» (Рассрочка)')
        preparation_transaction.fill_preparation_transaction_cc_passage_task()
        passage_preparation_transaction.go_task(driver)
        sign_agreement_client.fill_sign_agreement_client(driver)
        assert_db.assert_db_for_tariff_installment_and_2box(base_url, application_id)


class PassTask:

    def go_task(self, driver):
        # Взять задачу в работу через "Взять в работу" в заявке
        base_page = BasePage(driver)
        base_page.application_search(number_app=application_id)
        application_page = Application(driver)
        application_page.take_on_job_task()

    def passage_preparation_transaction(self, driver, tariff=None):
        # Проход до задачи Подготовка к сделке
        short_form = ShortFormPage(driver)
        global application_id
        application_id = short_form.determine_application_number()
        short_form.fill_required_fields_short_form(driver)
        self.go_task(driver)
        full_form = FullForm(driver)
        full_form.filling_required_fields_full_form_passage()
        self.go_task(driver)
        select_configure = SelectConfigure(driver)
        select_configure.choose_tariff_passage_task(tariff)
        self.go_task(driver)
        notify_client = NotifyClient(driver)
        notify_client.notify_client_passage_task()
        self.go_task(driver)





