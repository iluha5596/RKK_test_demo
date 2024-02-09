from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.application_list import ApplicationList
from pages.short_form import ShortFormPage
from pages.application import Application
from decouple import config


class PassageTask(BasePage):

    def __init__(self, driver, url=None, timeout=20):
        super().__init__(driver, url, timeout)
        self.number_app = None

    def application_search(self):
        # Переход на вкладку список заявок
        base_page = BasePage(self.driver)
        base_page.go_application_list()
        # Поиск заявки
        application_list_page = ApplicationList(self.driver)
        number_app = self.number_app
        application_list_page.search_application(number_app=number_app)

    def take_on_job_task(self):
        # Взять в работу задачу
        application_page = Application(self.driver)
        application_page.expectation_task()
        application_page.go_task()

    def create_task_short_form(self, base_url, path):
        base_url = base_url
        path = path
        url = f'{base_url}{path}'
        login_page = LoginPage(self.driver, url)
        login_page.open()
        # Авторизация
        login = config('LOGIN_CM_25')
        password = config('PASSWORD_CM_25')
        login_page.authorization(login=login, password=password)

    def fill_required_fields_short_form(self):
        # Заполнение обязательных полей на задаче Короткая анкета
        short_form_page = ShortFormPage(self.driver)
        short_form_page.filling_short_form()
        short_form_page.generate_documents()
        short_form_page.modal_window_generate_documents()
        base_page = BasePage(self.driver)
        base_page.close_new_window()
        short_form_page.attach_client_consent_file()
        short_form_page.next_form()
        self.number_app = short_form_page.determine_application_number()
        print(self.number_app)

    def full_form_pass(self, base_url, path):
        self.create_task_short_form(base_url, path)
        self.fill_required_fields_short_form()
        self.application_search()
        self.take_on_job_task()




