class YourClass:
    def __init__(self):
        # Инициализация атрибута класса для хранения номера заявки
        self.application_number = None

    def fill_required_fields_short_form(self):
        # Заполняем форму короткой анкеты и получаем номер заявки
        # Предположим, что ваш метод fill_required_fields_short_form возвращает номер заявки
        self.application_number = 'П_00114822'

        self.application_number = self.fill_required_fields_short_form()
        print(f"Application number: {self.application_number}")

    def application_search(self):
        # Используем номер заявки в методе application_search
        if self.application_number:
            print(f"Searching for application: {self.application_number}")
            # Дополнительные действия для поиска заявки
        else:
            print("Application number is not set. Please run fill_required_fields_short_form first.")
