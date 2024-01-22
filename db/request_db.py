import psycopg2
from psycopg2 import Error
from decouple import config


class DB(object):

    def __init__(self):
        # Инициализируем переменные, чтобы избежать ошибок
        self.connection = None
        self.select_query = None
        self.result = None

    def select_external_source(self, application_id, source):
        self.select_query = f"SELECT source, request_data FROM external_source es WHERE application_id = {application_id} AND es.source = '{source}' ORDER BY es.request_time DESC"

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
            self.get_result()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Соединение с PostgreSQL закрыто")

    def get_result(self):
        # Выводим значения столбцов для каждой строки
        for row in self.result:
            print(f"source: {row[0]}, request_data: {row[1]}")  # Замените индексы на фактические столбцы


# Пример использования
db_instance = DB()

db_instance.connect()
db_instance.select_external_source(114332, 'XBPM-PA-SENDSTATUS')
db_instance.request()

db_instance.connect()
db_instance.select_client(114332)
db_instance.request()




