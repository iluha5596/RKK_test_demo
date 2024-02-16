import json


class ReadSaveData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_data = self.read_data()

    def read_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def save_data(self, data):
        # Обновление current_index в объекте данных
        self.file_data['current_index'] = data
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self.file_data, file, indent=2)


class ShortFormData(ReadSaveData):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.amount_credit = self.file_data['amount_credit']
        self.monthly_income_amount = self.file_data['monthly_income_amount']


class FullFormData(ReadSaveData):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.credit_term = self.file_data['credit_term']
        self.phone = self.file_data['phone']
        self.children_count = self.file_data['children_count']
        self.depends_count = self.file_data['depends_count']
        self.employer_name = self.file_data['employer_name']
        self.years_experience = self.file_data['years_experience']
        self.months_experience = self.file_data['months_experience']
        self.position = self.file_data['position']
        self.employer_phone = self.file_data['employer_phone']


class PreparationTransactionData(ReadSaveData):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.count_box_solutions = self.file_data['count_box_solutions']
        self.contract_number_box_1 = self.file_data['contract_number_box_1']
        self.contract_number_box_2 = self.file_data['contract_number_box_2']
        self.codeword = self.file_data['codeword']
        self.id_card = self.file_data['id_card']
        self.current_index = self.file_data['current_index']
