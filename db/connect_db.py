import psycopg2
from decouple import config


class ConnectDB:

    def __init__(self):
        self.connection = None

    def connect(self):
        # Выполнение подключения к БД
        db_database = config('DB_DATABASE')
        db_port = config('DB_PORT')
        db_host = config('DB_HOST')
        db_username = config('DB_USERNAME')
        db_password = config('DB_PASSWORD')

        print(db_database)

        try:
            connection = psycopg2.connect(
                user=db_username,
                password=db_password,
                host=db_host,
                port=db_port,
                database=db_database
            )
            self.connection = connection
            print("Соединение с PostgreSQL установлено")
            return connection
        except Exception as error:
            print(f"Ошибка при подключении к PostgreSQL: {error}")


