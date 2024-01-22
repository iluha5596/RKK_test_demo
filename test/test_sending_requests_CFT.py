import time
import pytest
from pages.login_page import LoginPage
from decouple import config
from pages.application import Application
from pages.application_list import ApplicationList
from pages.short_form import ShortFormPage
from pages.base_page import BasePage
from pages.my_task import MyTask
from pages.full_form import FullForm
from pages.select_configure import SelectConfigure
from pages.notify_client import NotifyClient


class TestSendingRequestsCFT:
    # def test_your_function(self, driver, base_url, client_cft_id):
    #     base_url = base_url
    #     client_cft_id = client_cft_id
    #     url = f'{base_url}{client_cft_id}'
    #     login_page = LoginPage(driver, url)
    #     login_page.open()
    #     login = config('LOGIN_CM_25')
    #     password = config('PASSWORD_CM_25')
    #     login_page.authorization(login=login, password=password)
    #     short_form_page = ShortFormPage(driver, url)
    #     short_form_page.filling_short_form()
    #     short_form_page.generate_documents()
    #     short_form_page.modal_window_generate_documents()
    #     # short_form_page.next_form()
    #     time.sleep(30)

    @pytest.mark.skip
    def test_short_form_pass(self, driver, base_url, path):
        base_url = base_url
        path = path
        url = f'{base_url}{path}'
        login_page = LoginPage(driver, url)
        login_page.open()
        # Авторизация
        login = config('LOGIN_CM_25')
        password = config('PASSWORD_CM_25')
        login_page.authorization(login=login, password=password)
        number_app = 'П_00114632'
        # Поиск задачи через Мои задачи
        my_task_page = MyTask(driver)
        my_task_page.search_task(number_app=number_app)
        # Проход в задачу через  БЭФ
        application_page = Application(driver)
        application_page.go_task()
        # Работа с короткой формой
        short_form_page = ShortFormPage(driver)
        short_form_page.filling_short_form()
        short_form_page.generate_documents()
        short_form_page.modal_window_generate_documents()
        base_page = BasePage(driver)
        base_page.close_new_window()
        short_form_page.attach_client_consent_file()
        short_form_page.next_form()
        # Переход на вкладку список заявок
        base_page.go_application_list()
        # Поиск заявки после прохождения короткой формы
        application_list_page = ApplicationList(driver)
        application_list_page.search_application(number_app=number_app)
        # Взять в работу задачу Заполнить полную анкету
        application_page.expectation_task()
        application_page.go_task()
        time.sleep(20)

    @pytest.mark.skip
    def test_full_form_pass(self, driver, base_url, path):
        base_url = base_url
        path = path
        url = f'{base_url}{path}'
        login_page = LoginPage(driver, url)
        login_page.open()
        # Авторизация
        login = config('LOGIN_CM_25')
        password = config('PASSWORD_CM_25')
        login_page.authorization(login=login, password=password)
        number_app = 'П_00114613'
        # Поиск задачи через Мои задачи
        my_task_page = MyTask(driver)
        my_task_page.search_task(number_app=number_app)
        # Проход в задачу через  БЭФ
        application_page = Application(driver)
        application_page.go_task()
        # Заполнение обязательных полей на полной форме
        full_form = FullForm(driver)
        full_form.filling_required_fields_full_form()
        full_form.full_app_next_form()

    @pytest.mark.skip
    def test_select_config_pass(self, driver, base_url, path):
        base_url = base_url
        path = path
        url = f'{base_url}{path}'
        login_page = LoginPage(driver, url)
        login_page.open()
        # Авторизация
        login = config('LOGIN_CM_25')
        password = config('PASSWORD_CM_25')
        login_page.authorization(login=login, password=password)
        number_app = 'П_00114363'
        # Поиск задачи через Мои задачи
        my_task_page = MyTask(driver)
        my_task_page.search_task(number_app=number_app)
        # Проход в задачу через  БЭФ
        application_page = Application(driver)
        application_page.go_task()
        # Выбор тарифа и отправка заявки далее по процессу
        select_configure_page = SelectConfigure(driver)
        select_configure_page.choose_privilege_credit_card_installment()
        select_configure_page.choose_transition_decision_making()
        select_configure_page.select_configure_next_form()
        # Переход на вкладку список заявок
        base_page = BasePage(driver)
        base_page.go_application_list()
        # Поиск заявки
        application_list_page = ApplicationList(driver)
        application_list_page.search_application(number_app=number_app)
        # Взять в работу задачу Уведомить клиента
        application_page.expectation_task()
        application_page.go_task()
        time.sleep(60)

    @pytest.mark.skip
    def test_notify_client_pass(self, driver, base_url, path):
        base_url = base_url
        path = path
        url = f'{base_url}{path}'
        login_page = LoginPage(driver, url)
        login_page.open()
        # Авторизация
        login = config('LOGIN_CM_25')
        password = config('PASSWORD_CM_25')
        login_page.authorization(login=login, password=password)
        number_app = 'П_00114592'
        # Поиск задачи через Мои задачи
        my_task_page = MyTask(driver)
        my_task_page.search_task(number_app=number_app)
        # Проход в задачу через  БЭФ
        application_page = Application(driver)
        application_page.go_task()
        # Отправить заявку далее по процессу с Уведомить клиента
        notify_client_page = NotifyClient(driver)
        notify_client_page.choose_client_agrees()
        notify_client_page.notify_client_next_form()
        # Переход на вкладку список заявок
        base_page = BasePage(driver)
        base_page.go_application_list()
        # Поиск заявки после прохождения Уведомить клиента
        application_list_page = ApplicationList(driver)
        application_list_page.search_application(number_app=number_app)
        # Взять в работу задачу Подготовка к сделке
        application_page.expectation_task()
        application_page.go_task()
        time.sleep(80)

    # @pytest.mark.skip
    def test_pass_preparation_deal(self, driver, base_url, path):
        base_url = base_url
        path = path
        url = f'{base_url}{path}'
        login_page = LoginPage(driver, url)
        login_page.open()
        # Авторизация
        login = config('LOGIN_CM_25')
        password = config('PASSWORD_CM_25')
        login_page.authorization(login=login, password=password)
        number_app = 'П_00114822'
        # Поиск задачи через Мои задачи
        my_task_page = MyTask(driver)
        my_task_page.search_task(number_app=number_app)
        # Проход в задачу через  БЭФ
        application_page = Application(driver)
        application_page.go_task()
        # Работа с короткой формой
        short_form_page = ShortFormPage(driver)
        short_form_page.filling_short_form()
        short_form_page.generate_documents()
        short_form_page.modal_window_generate_documents()
        base_page = BasePage(driver)
        base_page.close_new_window()
        short_form_page.attach_client_consent_file()
        short_form_page.next_form()
        # Переход на вкладку список заявок
        base_page.go_application_list()
        # Поиск заявки после прохождения короткой формы
        application_list_page = ApplicationList(driver)
        application_list_page.search_application(number_app=number_app)
        # Взять в работу задачу Заполнить полную анкету
        application_page.expectation_task()
        application_page.go_task()
        # Заполнение обязательных полей на полной форме
        full_form = FullForm(driver)
        full_form.filling_required_fields_full_form()
        full_form.full_app_next_form()
        # Переход на вкладку список заявок
        base_page.go_application_list()
        # Поиск заявки
        application_list_page.search_application(number_app=number_app)
        # Взять в работу задачу Выбрать и сконфигрурировать
        application_page.expectation_task()
        application_page.go_task()
        # Выбор тарифа и отправка заявки далее по процессу
        select_configure_page = SelectConfigure(driver)
        select_configure_page.choose_privilege_credit_card_installment()
        select_configure_page.choose_transition_decision_making()
        select_configure_page.select_configure_next_form()
        # Переход на вкладку список заявок
        base_page.go_application_list()
        # Поиск заявки
        application_list_page.search_application(number_app=number_app)
        # Взять в работу задачу Уведомить клиента
        application_page.expectation_task()
        application_page.go_task()
        # Отправить заявку далее по процессу с Уведомить клиента
        notify_client_page = NotifyClient(driver)
        notify_client_page.choose_client_agrees()
        notify_client_page.notify_client_next_form()
        # Переход на вкладку список заявок
        base_page = BasePage(driver)
        base_page.go_application_list()
        # Поиск заявки после прохождения Уведомить клиента
        application_list_page = ApplicationList(driver)
        application_list_page.search_application(number_app=number_app)
        # Взять в работу задачу Подготовка к сделке
        application_page.expectation_task()
        application_page.go_task()














