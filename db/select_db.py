

class SelectDB:

    def __init__(self):
        self.select_query = None

    def select_external_source(self, application_id=None):
        self.select_query = f"SELECT stage, source, request_status, request_time, response_time " \
                            f"FROM external_source es " \
                            f"JOIN application a on (es.application_id = a.id) " \
                            f"WHERE a.number = '{application_id}' order by es.request_time desc "

    def select_response_data(self, application_id=None, source=None):
        self.select_query = f"SELECT response_data " \
                            f"FROM external_source es " \
                            f"JOIN application a on (es.application_id = a.id) " \
                            f"WHERE a.number = '{application_id}' " \
                            f"AND es.source = '{source}' "

    def select_request_data(self, application_id=None, source=None):
        self.select_query = f"SELECT request_data " \
                            f"FROM external_source es " \
                            f"JOIN application a on (es.application_id = a.id) " \
                            f"WHERE a.number = '{application_id}' " \
                            f"AND es.source = '{source}' "

    def select_count_method_calls(self, application_id=None, source=None):
        self.select_query = f"SELECT count('{source}') " \
                            f"FROM external_source es " \
                            f"JOIN application a on (es.application_id = a.id) " \
                            f"WHERE a.number = '{application_id}' " \
                            f"AND es.source = '{source}' "

    def select_account_number(self, application_id=None):
        self.select_query = f"SELECT account_number from issue_terms it " \
                            f"JOIN application a on (it.application_id = a.id) " \
                            f"WHERE a.number = '{application_id}' " \
                            f"AND it.is_actual "
