from db.select_db import SelectDB
from db.request_db import RequestDB
import re


class GetResultDB(object):

    def res_value_create_account(self, application_id, source):
        select_db = SelectDB()
        select_db.select_response_data(application_id=application_id, source=source)
        request_db = RequestDB()
        result = request_db.request(select_db.select_query)
        pattern = r'<ResValue>(.*?)</ResValue>'
        matches = []
        # Используем регулярное выражение для поиска совпадений в каждой строке результата
        for row in result:
            match = re.search(pattern, row[0])  # Поиск по первому столбцу
            if match:
                matches.append(match.group(1))  # Добавляем найденное значение
        self.matches = matches
        return self.matches

    def request(self, application_id, source, compiler):
        select_db = SelectDB()
        select_db.select_request_data(application_id=application_id, source=source)
        request_db = RequestDB()
        result = request_db.request(select_db.select_query)
        pattern = compiler
        matches = []
        for response in result:
            match = pattern.search(response[0])
            if match:
                matches.append(match.group(1))
        self.matches = matches
        return self.matches


    def request_count_method_calls(self, application_id, source):
        # Получаем количество вызовов определённого метода
        select_db = SelectDB()
        select_db.select_count_method_calls(application_id=application_id, source= source)
        request_db = RequestDB()
        result = request_db.request(select_db.select_query)
        value = result[0][0]
        self.value = value
        return value


class AssertDB(object):

    def assert_cft_updateaccount(self):
        get_result_db = GetResultDB()
        # Получаем значение transfer_account из ответа от метода CFT_CREATE_ACCOUNT
        transfer_account_create_account = get_result_db.res_value_create_account(application_id=111210, source='CFT_CREATE_ACCOUNT')
        # Получаем значение transfer_account из запроса в метод XBPM_CFT_UPDATEACCOUNT
        compiler = re.compile(r'<ns2:RECEIVER_ACC>(.*?)</ns2:RECEIVER_ACC>', re.DOTALL)
        transfer_account_update_account = get_result_db.request(application_id=111210, source='XBPM_CFT_UPDATEACCOUNT', compiler=compiler)
        assert transfer_account_create_account == transfer_account_update_account, 'В XBPM_CFT_UPDATEACCOUNT передался ' \
                                                                                   'не верный transfer_account'

    def assert_count_method_calls(self, count_calls=3):
        get_result_db = GetResultDB()
        count_method_calls = get_result_db.request_count_method_calls(application_id=111210, source='XBPM_CFT_TRANSFERCARD')
        assert count_method_calls == count_calls, f"Метод XBPM_CFT_TRANSFERCARD должен был вызваться {count_calls} раз(а)," \
                                                  f"по итогу вызвался {count_method_calls} раз(а)"

    def assert_sender_acc_transfer_card(self):
        get_result_db = GetResultDB()
        compiler = re.compile(r'<ns2:DOC_TYPE>TRANSFER_INSTALLMENT</ns2:DOC_TYPE>.*?<ns2:SENDER_ACC>(.*?)</ns2:SENDER_ACC>', re.DOTALL)
        sender_acc_transfer_card = get_result_db.request(application_id=111210, source='XBPM_CFT_TRANSFERCARD', compiler=compiler)
        print(sender_acc_transfer_card)


assert_db = AssertDB()
assert_db.assert_cft_updateaccount()
