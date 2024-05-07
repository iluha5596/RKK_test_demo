import allure
import pytest
from pages.login_page import LoginPage
from decouple import config
from pages.application import Application
from pages.short_form import ShortFormPage
from pages.full_form import FullForm
from pages.select_configure import SelectConfigure
from pages.notify_client import NotifyClient
from pages.preparation_transaction import PreparationTransaction
from pages.sign_agreement_client import SignAgreementClient
from db.assert_db import AssertDB


def passage_preparation_transaction(driver, tariff=None):
    # Проход до задачи Подготовка к сделке
    short_form = ShortFormPage(driver)
    application = Application(driver)
    short_form.determine_application_number()
    short_form.fill_required_fields_short_form(driver)
    application.take_task_through_application_form(driver)
    full_form = FullForm(driver)
    full_form.filling_required_fields_full_form_passage()
    application.take_task_through_application_form(driver)
    select_configure = SelectConfigure(driver)
    select_configure.choose_tariff_passage_task(tariff)
    application.take_task_through_application_form(driver)
    notify_client = NotifyClient(driver)
    notify_client.notify_client_passage_task()
    application.take_task_through_application_form(driver)


@allure.feature('Тестирование CFT методов')
class TestCFTMethod:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver, base_url, path):
        url = f'{base_url[0]}{path}'
        print(url)
        login_page = LoginPage(driver, url)
        login_page.open()
        # Авторизация
        login = config('LOGIN_CM_25')
        password = config('PASSWORD_CM_25')
        login_page.authorization(login=login, password=password)

    @allure.story('Тестирование тарифа с рассрочкой и двумя одинаковыми коробками')
    def test_tariff_installment_and_2box(self, driver, base_url):
        preparation_transaction = PreparationTransaction(driver)
        sign_agreement_client = SignAgreementClient(driver)
        short_form_page = ShortFormPage(driver)
        application = Application(driver)
        assert_db = AssertDB()
        passage_preparation_transaction(driver, tariff='«Кредитная «Карта Привилегий» (Рассрочка)')
        preparation_transaction.fill_preparation_transaction_cc_passage_task()
        application.take_task_through_application_form(driver)
        sign_agreement_client.fill_sign_agreement_client(driver)
        assert_db.assert_db_for_tariff_installment_and_2box(base_url, application_id=short_form_page.application_id)
