from db.select_db import SelectDB
from db.request_db import RequestDB
import time
import re


class GetResultDB(object):

    def res_value_create_account(self, source, compiler, base_url, application_id):
        # Получаем результыт ответов методов
        select_db = SelectDB()
        select_db.select_response_data(application_id=application_id, source=source)
        request_db = RequestDB()
        result = request_db.request(select_db.select_query, base_url=base_url)
        pattern = compiler
        matches = []
        # Используем регулярное выражение для поиска совпадений в каждой строке результата
        for row in result:
            match = re.search(pattern, row[0])  # Поиск по первому столбцу
            if match:
                matches.append(match.group(1))  # Добавляем найденное значение
        value = ''.join(matches)
        return value

    def external_source_request(self, source, compiler, base_url, application_id):
        # Получаем результаты запросов методов
        select_db = SelectDB()
        select_db.select_request_data(application_id=application_id, source=source)
        request_db = RequestDB()
        result = request_db.request(select_db.select_query, base_url=base_url)
        pattern = compiler
        matches = []
        for response in result:
            match = pattern.search(response[0])
            if match:
                matches.append(match.group(1))
        return matches

    def request_count_method_calls(self, source, base_url, application_id):
        # Получаем количество вызовов определённого метода
        select_db = SelectDB()
        select_db.select_count_method_calls(application_id=application_id, source=source)
        request_db = RequestDB()
        result = request_db.request(select_db.select_query, base_url=base_url)
        value_count_method_calls = result[0][0]
        return value_count_method_calls

    def account_number(self, base_url, application_id):
        # Получаем account_number
        select_db = SelectDB()
        select_db.select_account_number(application_id=application_id)
        request_db = RequestDB()
        result = request_db.request(select_db.select_query, base_url=base_url)
        value_account_number = result[0][0]
        return value_account_number


class AssertDB(object):

    def assert_db_for_tariff_installment_and_2box(self, base_url, application_id):
        # Проверки БД для теста с тарифом рассрочка и двумя коробками
        self.wait_close_process(base_url, application_id)
        self.assert_cft_updateaccount(base_url, application_id)
        self.assert_count_method_calls(base_url, application_id)
        self.assert_transfer_installment(base_url, application_id)
        self.assert_payment_box(base_url, application_id)
        print('Проверки БД успешно прошли')

    def wait_close_process(self, base_url, application_id):
        get_result_db = GetResultDB()
        count_method_calls = get_result_db.request_count_method_calls(source='MG_SENDMESSAGE',
                                                                      base_url=base_url,
                                                                      application_id=application_id)
        while count_method_calls < 2:
            count_method_calls = get_result_db.request_count_method_calls(source='MG_SENDMESSAGE',
                                                                          base_url=base_url,
                                                                          application_id=application_id)
            print('Процесс ещё не завершился')
            time.sleep(5)
        print('Процесс завершился, стартауют проверки БД')

    def assert_cft_updateaccount(self, base_url, application_id):
        get_result_db = GetResultDB()
        # Получаем значение transfer_account из ответа от метода CFT_CREATE_ACCOUNT
        compiler = re.compile(r'<ResValue>(.*?)</ResValue>', re.DOTALL)
        transfer_account = get_result_db.res_value_create_account(source='CFT_CREATE_ACCOUNT',
                                                                  compiler=compiler,
                                                                  base_url=base_url,
                                                                  application_id=application_id)
        # Получаем значение transfer_account из запроса в метод XBPM_CFT_UPDATEACCOUNT
        compiler = re.compile(r'<ns2:RECEIVER_ACC>(.*?)</ns2:RECEIVER_ACC>', re.DOTALL)
        receiver_acc_updateaccount = get_result_db.external_source_request(source='XBPM_CFT_UPDATEACCOUNT',
                                                                           compiler=compiler,
                                                                           base_url=base_url,
                                                                           application_id=application_id)
        value_receiver_acc_updateaccount = ' '.join(receiver_acc_updateaccount)
        assert transfer_account == value_receiver_acc_updateaccount, \
            'В XBPM_CFT_UPDATEACCOUNT передался не верный transfer_account'
        self.transfer_account = transfer_account

    def assert_count_method_calls(self, base_url, application_id, count_calls=3):
        get_result_db = GetResultDB()
        count_method_calls = get_result_db.request_count_method_calls(source='XBPM_CFT_TRANSFERCARD',
                                                                      base_url=base_url,
                                                                      application_id=application_id)
        assert count_method_calls == count_calls, \
            f"Метод XBPM_CFT_TRANSFERCARD должен был вызваться {count_calls} раз(а), по итогу вызвался {count_method_calls} раз(а)"

    def assert_transfer_installment(self, base_url, application_id):
        get_result_db = GetResultDB()
        compiler = re.compile(r'<ns2:DOC_TYPE>TRANSFER_INSTALLMENT</ns2:DOC_TYPE>.*?<ns2:SENDER_ACC>(.*?)</ns2:SENDER_ACC>', re.DOTALL)
        sender_acc_transfer_card = get_result_db.external_source_request(source='XBPM_CFT_TRANSFERCARD',
                                                                         compiler=compiler,
                                                                         base_url=base_url,
                                                                         application_id=application_id)
        value_sender_acc_transfer_card = ' '.join(sender_acc_transfer_card)
        account_number = get_result_db.account_number(base_url=base_url, application_id=application_id)
        assert value_sender_acc_transfer_card == account_number, \
            'В XBPM_CFT_TRANSFERCARD по услуге TRANSFER_INSTALLMENT передался не верный SENDER_ACC (account_number)'
        compiler = re.compile(r'<ns2:DOC_TYPE>TRANSFER_INSTALLMENT</ns2:DOC_TYPE>.*?<ns2:RECEIVER_ACC>(.*?)</ns2:RECEIVER_ACC>', re.DOTALL)
        receiver_acc_transfer_card = get_result_db.external_source_request(source='XBPM_CFT_TRANSFERCARD',
                                                                           compiler=compiler,
                                                                           base_url=base_url,
                                                                           application_id=application_id)
        value_receiver_acc_transfer_card = ''.join(receiver_acc_transfer_card)
        assert value_receiver_acc_transfer_card == self.transfer_account, \
            'В XBPM_CFT_TRANSFERCARD по услуге TRANSFER_INSTALLMENT передался не верный RECEIVER_ACC (transfer_account)'

    def assert_payment_box(self, base_url, application_id):
        get_result_db = GetResultDB()
        compiler = re.compile(r'<ns2:DOC_TYPE>PAYMENT_BOX</ns2:DOC_TYPE>.*?<ns2:SENDER_ACC>(.*?)</ns2:SENDER_ACC>', re.DOTALL)
        sender_acc_payment_box = get_result_db.external_source_request(source='XBPM_CFT_TRANSFERCARD',
                                                                       compiler=compiler,
                                                                       base_url=base_url,
                                                                       application_id=application_id)
        for value_sender_acc_payment_box in sender_acc_payment_box:
            assert value_sender_acc_payment_box == self.transfer_account, \
                'В XBPM_CFT_TRANSFERCARD по услуге PAYMENT_BOX передался не верный SENDER_ACC (transfer_account)'

        compiler = re.compile(r'<ns2:DOC_TYPE>PAYMENT_BOX</ns2:DOC_TYPE>.*?<ns2:DESCRIPTION>(.*?)</ns2:DESCRIPTION>', re.DOTALL)
        description_payment_box = get_result_db.external_source_request(source='XBPM_CFT_TRANSFERCARD',
                                                                        compiler=compiler,
                                                                        base_url=base_url,
                                                                        application_id=application_id)
        for i in range(len(description_payment_box)):
            for j in range(i+1, len(description_payment_box)):
                assert description_payment_box[i] != description_payment_box[j], \
                    'В XBPM_CFT_TRANSFERCARD по услуге PAYMENT_BOX отправилось значение по одной и той же коробке, а должно было по двум'

