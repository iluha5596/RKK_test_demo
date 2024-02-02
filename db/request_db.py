import psycopg2
from psycopg2 import Error
from decouple import config
import re


class RequestDB(object):

    def __init__(self):
        # Инициализируем переменные
        self.connection = None
        self.select_query = None
        self.result = None

    def select_external_source(self, application_id=None):
        self.select_query = f"SELECT stage, source, request_status, request_time, response_time from external_source es where application_id = {application_id} order by es.request_time desc"

    def select_response_data(self, application_id=None, source=None):
        self.select_query = f"SELECT response_data FROM external_source es WHERE application_id = {application_id} AND es.source = '{source}' ORDER BY es.request_time DESC"

    def select_request_data(self, application_id=None, source=None):
        self.select_query = f"SELECT request_data FROM external_source es WHERE application_id = {application_id} AND es.source = '{source}' ORDER BY es.request_time DESC"

    def select_count_method_calls(self, application_id=None, source=None):
        self.select_query = f"SELECT count(source) from external_source es where application_id = {application_id} and es.source = '{source}'"

    def select_client(self, application_id):
        self.select_query = f"select * from client c where application_id = {application_id}"

    def connect(self):
        db_database = config('DB_DATABASE')
        db_port = config('DB_PORT')
        db_host = config('DB_HOST')
        db_username = config('DB_USERNAME')
        db_password = config('DB_PASSWORD')

        try:
            self.connection = psycopg2.connect(
                user=db_username,
                password=db_password,
                host=db_host,
                port=db_port,
                database=db_database
            )
            print("Соединение с PostgreSQL установлено")
        except Exception as error:
            print(f"Ошибка при подключении к PostgreSQL: {error}")

    def request(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(self.select_query)
            # Получаем все строки результата
            result = cursor.fetchall()
            self.result = result
            return result
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Соединение с PostgreSQL закрыто")


class AssertDB(object):

    def response_cft_create_account(self):
        # Получаем значение transfer_account из ответа от метода CFT_CREATE_ACCOUNT
        db_instance = RequestDB()
        db_instance.connect()  # Подключаемся к базе данных
        db_instance.select_response_data(application_id=111210, source='CFT_CREATE_ACCOUNT')
        result = db_instance.request()  # Получаем результат запроса
        pattern = r'<ResValue>(.*?)</ResValue>'
        # Используем регулярное выражение для поиска совпадений в каждой строке результата
        matches = []
        for row in result:
            match = re.search(pattern, row[0])  # Поиск по первому столбцу
            if match:
                matches.append(match.group(1))  # Добавляем найденное значение
        self.matches = matches
        print(self.matches)

    def request_cft_update_client(self):
        # Получаем значение transfer_account из запроса в метод CFT_UPDATE_CLIENT
        db_instance = RequestDB()
        db_instance.connect()  # Подключаемся к базе данных
        db_instance.select_request_data(application_id=111210, source='XBPM_CFT_UPDATEACCOUNT')
        result = db_instance.request()  # Получаем результат запроса
        pattern = r'<ns2:RECEIVER_ACC>(.*?)</ns2:RECEIVER_ACC>'
        # Используем регулярное выражение для поиска совпадений в каждой строке результата
        matches = []
        for row in result:
            match = re.search(pattern, row[0])  # Поиск по первому столбцу
            if match:
                matches.append(match.group(1))  # Добавляем найденное значение
        self.matches = matches
        print(self.matches)

    def request_count_method_calls(self):
        # Получаем количество вызовов определённого метода
        db_instance = RequestDB()
        db_instance.connect()  # Подключаемся к базе данных
        db_instance.select_count_method_calls(application_id=111210, source='XBPM_CFT_TRANSFERCARD')
        result = db_instance.request()  # Получаем результат запроса
        value = result[0][0]
        self.value = value
        print(f'Кол-во запросов в метод: {value}')





    def assert_db_tariff_installment_and_2box(self):
        db_instance = RequestDB()
        db_instance.connect()  # Подключаемся к базе данных
        db_instance.select_response_data(application_id=111210, source='CFT_CREATE_ACCOUNT')


# Создаем экземпляр класса AssertDB
assert_db = AssertDB()
# Вызываем метод check_db() у созданного экземпляра
assert_db.request_count_method_calls()

# db_instance = RequestDB()
# db_instance.connect()  # Подключаемся к базе данных
# db_instance.select_external_source(111210)
# db_instance.request()  # Выполняем запрос к базе данных

# db_instance.select_external_source(111210)
# db_instance.select_external_source(111210, 'XBPM-PA-SENDSTATUS')
#

# db_instance.connect()
# db_instance.select_client(114332)
# db_instance.request()
