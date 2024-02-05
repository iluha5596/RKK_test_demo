from db.select_db import SelectDB
from db.request_db import RequestDB
import re


class GetResultDB(object):

    def res_value_create_account(self, application_id, source, compiler):
        # Получаем результыт ответов методов
        select_db = SelectDB()
        select_db.select_response_data(application_id=application_id, source=source)
        request_db = RequestDB()
        result = request_db.request(select_db.select_query)
        pattern = compiler
        matches = []
        # Используем регулярное выражение для поиска совпадений в каждой строке результата
        for row in result:
            match = re.search(pattern, row[0])  # Поиск по первому столбцу
            if match:
                matches.append(match.group(1))  # Добавляем найденное значение
        # self.matches = matches
        value = ''.join(matches)
        return value

    def external_source_request(self, application_id, source, compiler):
        # Получаем результаты запросов методов
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
        return matches

    def request_count_method_calls(self, application_id, source):
        # Получаем количество вызовов определённого метода
        select_db = SelectDB()
        select_db.select_count_method_calls(application_id=application_id, source= source)
        request_db = RequestDB()
        result = request_db.request(select_db.select_query)
        value_count_method_calls = result[0][0]
        # self.value = value
        return value_count_method_calls

    def account_number(self, application_id):
        # Получаем account_number
        select_db = SelectDB()
        select_db.select_account_number(application_id=application_id)
        request_db = RequestDB()
        result = request_db.request(select_db.select_query)
        value_account_number = result[0][0]
        return value_account_number


class AssertDB(object):

    # def wait_close_process(self, application_id):
    #     get_result_db = GetResultDB()
    #     count_method_calls = get_result_db.request_count_method_calls(application_id=application_id, source='MG_SENDMESSAGE')
    #     while count_method_calls < 2:
    #         get_result_db.request_count_method_calls(application_id=application_id, source='MG_SENDMESSAGE')
    #         print(f'Процесс ещё не завершился. Количество вызовов MG_SENDMESSAGE = {count_method_calls}, ожидается, что будет 2')
    #     print(f'Процесс завершился, можно делать проверки БД, MG_SENDMESSAGE = {count_method_calls}')


    def assert_db_for_tariff_installment_and_2box(self, application_id):
        self.assert_cft_updateaccount(application_id)
        self.assert_count_method_calls(application_id)
        self.assert_transfer_installment(application_id)
        self.assert_payment_box(application_id)


    def assert_cft_updateaccount(self, application_id):
        get_result_db = GetResultDB()
        # Получаем значение transfer_account из ответа от метода CFT_CREATE_ACCOUNT
        compiler = re.compile(r'<ResValue>(.*?)</ResValue>', re.DOTALL)
        transfer_account = get_result_db.res_value_create_account(application_id=application_id, source='CFT_CREATE_ACCOUNT', compiler=compiler)
        # Получаем значение transfer_account из запроса в метод XBPM_CFT_UPDATEACCOUNT
        compiler = re.compile(r'<ns2:RECEIVER_ACC>(.*?)</ns2:RECEIVER_ACC>', re.DOTALL)
        receiver_acc_updateaccount = get_result_db.external_source_request(application_id=application_id, source='XBPM_CFT_UPDATEACCOUNT', compiler=compiler)
        value_receiver_acc_updateaccount = ' '.join(receiver_acc_updateaccount)
        assert transfer_account == value_receiver_acc_updateaccount, 'В XBPM_CFT_UPDATEACCOUNT передался ' \
                                                                                   'не верный transfer_account'
        self.transfer_account = transfer_account

    def assert_count_method_calls(self, application_id, count_calls=4):
        get_result_db = GetResultDB()
        count_method_calls = get_result_db.request_count_method_calls(application_id=application_id, source='XBPM_CFT_TRANSFERCARD')
        assert count_method_calls == count_calls, f"Метод XBPM_CFT_TRANSFERCARD должен был вызваться {count_calls} раз(а)," \
                                                  f"по итогу вызвался {count_method_calls} раз(а)"

    def assert_transfer_installment(self, application_id):
        get_result_db = GetResultDB()
        compiler = re.compile(r'<ns2:DOC_TYPE>TRANSFER_INSTALLMENT</ns2:DOC_TYPE>.*?<ns2:SENDER_ACC>(.*?)</ns2:SENDER_ACC>', re.DOTALL)
        sender_acc_transfer_card = get_result_db.external_source_request(application_id=application_id, source='XBPM_CFT_TRANSFERCARD', compiler=compiler)
        value_sender_acc_transfer_card = ' '.join(sender_acc_transfer_card)
        account_number = get_result_db.account_number(application_id=application_id)
        assert value_sender_acc_transfer_card == account_number, 'В XBPM_CFT_TRANSFERCARD по услуге TRANSFER_INSTALLMENT передался не верный SENDER_ACC (account_number)'
        compiler = re.compile(r'<ns2:DOC_TYPE>TRANSFER_INSTALLMENT</ns2:DOC_TYPE>.*?<ns2:RECEIVER_ACC>(.*?)</ns2:RECEIVER_ACC>', re.DOTALL)
        receiver_acc_transfer_card = get_result_db.external_source_request(application_id=application_id, source='XBPM_CFT_TRANSFERCARD', compiler=compiler)
        value_receiver_acc_transfer_card = ''.join(receiver_acc_transfer_card)
        assert value_receiver_acc_transfer_card == self.transfer_account, 'В XBPM_CFT_TRANSFERCARD по услуге TRANSFER_INSTALLMENT передался не верный RECEIVER_ACC (transfer_account)'

    def assert_payment_box(self, application_id):
        get_result_db = GetResultDB()
        compiler = re.compile(r'<ns2:DOC_TYPE>PAYMENT_BOX</ns2:DOC_TYPE>.*?<ns2:SENDER_ACC>(.*?)</ns2:SENDER_ACC>', re.DOTALL)
        sender_acc_payment_box = get_result_db.external_source_request(application_id=application_id, source='XBPM_CFT_TRANSFERCARD', compiler=compiler)
        for value_sender_acc_payment_box in sender_acc_payment_box:
            assert value_sender_acc_payment_box == self.transfer_account, 'В XBPM_CFT_TRANSFERCARD по услуге PAYMENT_BOX передался не верный SENDER_ACC (transfer_account)'

        compiler = re.compile(r'<ns2:DOC_TYPE>PAYMENT_BOX</ns2:DOC_TYPE>.*?<ns2:DESCRIPTION>(.*?)</ns2:DESCRIPTION>', re.DOTALL)
        description_payment_box = get_result_db.external_source_request(application_id=application_id, source='XBPM_CFT_TRANSFERCARD', compiler=compiler)
        for i in range(len(description_payment_box)):
            for j in range(i+1, len(description_payment_box)):
                assert description_payment_box[i] != description_payment_box[j], 'В XBPM_CFT_TRANSFERCARD по услуге PAYMENT_BOX отправилось значение по одной и той же коробке, а должно было по двум'

