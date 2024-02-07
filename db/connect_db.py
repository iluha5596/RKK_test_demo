import psycopg2
from decouple import config


class ConnectDB:

    def __init__(self):
        self.connection = None

    def connect(self, base_url):
        # Выполнение подключения к БД
        db_database = config(f'DB_DATABASE_{base_url[1]}')
        db_port = config('DB_PORT')
        db_host = config(f'DB_HOST_{base_url[1]}')
        db_username = config(f'DB_USERNAME_{base_url[1]}')
        db_password = config(f'DB_PASSWORD_{base_url[1]}')

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


