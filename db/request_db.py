from db.connect_db import ConnectDB


class RequestDB(object):

    def __init__(self):
        self.result = None

    def request(self, select_query, base_url):
        connect_db = ConnectDB()
        connect_db.connect(base_url=base_url)
        cursor = connect_db.connection.cursor()
        try:
            cursor.execute(select_query)
            result = cursor.fetchall()
            self.result = result
            return result
        except Exception as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connect_db.connection:
                cursor.close()
                connect_db.connection.close()
                print("Соединение с PostgreSQL закрыто")





