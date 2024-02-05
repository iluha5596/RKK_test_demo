

class SelectDB:

    def __init__(self):
        self.select_query = None

    def select_external_source(self, application_id=None):
        self.select_query = f"SELECT stage, source, request_status, request_time, response_time " \
                            f"from external_source es " \
                            f"WHERE application_id = {application_id} order by es.request_time desc"

    def select_response_data(self, application_id=None, source=None):
        self.select_query = f"SELECT response_data " \
                            f"FROM external_source es " \
                            f"WHERE application_id = {application_id} " \
                            f"AND es.source = '{source}' ORDER BY es.request_time DESC"

    def select_request_data(self, application_id=None, source=None):
        self.select_query = f"SELECT request_data " \
                            f"FROM external_source es " \
                            f"WHERE application_id = {application_id} " \
                            f"AND es.source = '{source}' ORDER BY es.request_time DESC"

    def select_count_method_calls(self, application_id=None, source=None):
        self.select_query = f"SELECT count(source) " \
                            f"from external_source es " \
                            f"WHERE application_id = {application_id} " \
                            f"AND es.source = '{source}'"

    def select_account_number(self, application_id=None):
        self.select_query = f"select account_number from issue_terms " \
                            f"where application_id = {application_id} " \
                            f"and is_actual "

    def select_client(self, application_id):
        self.select_query = f"select * " \
                            f"from client c " \
                            f"WHERE application_id = {application_id}"