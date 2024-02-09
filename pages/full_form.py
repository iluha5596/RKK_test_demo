import json
import os
import time
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.full_form_locators import FullFormLocators


def read_data_full_form():
    file_full_form_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'data', 'data_full_form.json'))
    with open(file_full_form_path, 'r', encoding='utf-8') as file:
        data_full_form = json.load(file)

    credit_term = data_full_form['credit_term']
    phone = data_full_form['phone']
    children_count = data_full_form['children_count']
    depends_count = data_full_form['depends_count']
    employer_name = data_full_form['employer_name']
    years_experience = data_full_form['years_experience']
    months_experience = data_full_form['months_experience']
    position = data_full_form['position']
    employer_phone = data_full_form['employer_phone']

    return {'credit_term': credit_term, 'phone': phone, 'employer_name': employer_name,
            'children_count': children_count,
            'depends_count': depends_count, 'years_experience': years_experience,
            'months_experience': months_experience,
            'position': position, 'employer_phone': employer_phone}


class FullForm(BasePage):

    def filling_required_fields_full_form_passage(self):
        # Заполнение обязательных полей, отправить заявку далее по процессу
        self.filling_required_fields_full_form()
        self.full_app_next_form()

    def filling_required_fields_full_form(self):
        data_full_form = read_data_full_form()
        # Запрашиваемые условия
        self.visibility_of_element_located(*FullFormLocators.CREDIT_TERM)
        credit_term = self.driver.find_element(*FullFormLocators.CREDIT_TERM)
        credit_term.send_keys(data_full_form['credit_term'])
        purpose_credit = self.driver.find_element(*FullFormLocators.PURPOSE_CREDIT)
        purpose_credit.click()
        purpose_credit_car = self.driver.find_element(*FullFormLocators.PURPOSE_CREDIT_CAR)
        purpose_credit_car.click()
        # Инофрмация по клиенту
        family_status = self.driver.find_element(*FullFormLocators.FAMILY_STATUS)
        self.driver.execute_script('arguments[0].click();', family_status)
        family_status_never_married = self.driver.find_element(*FullFormLocators.FAMILY_STATUS_NEVER_MARRIED)
        family_status_never_married.click()
        children_count = self.driver.find_element(*FullFormLocators.COUNT_CHILDREN)
        children_count.send_keys(data_full_form['children_count'])
        depends_count = self.driver.find_element(*FullFormLocators.DEPENDS_COUNT)
        depends_count.send_keys(data_full_form['depends_count'])
        # Телефон контактного лица
        phone_contact_person = self.driver.find_element(*FullFormLocators.PHONE_CONTACT_PERSON)
        data_full_form_phone = data_full_form['phone']
        self.driver.execute_script("arguments[0].value = arguments[1];", phone_contact_person, data_full_form_phone)
        phone_contact_person.send_keys(data_full_form_phone, Keys.RETURN)
        # Адреса
        reasons_residence = self.driver.find_element(*FullFormLocators.REASONS_RESIDENCE)
        self.driver.execute_script('arguments[0].click();', reasons_residence)
        basis_residence_own = self.driver.find_element(*FullFormLocators.BASIS_RESIDENCE_OWN)
        basis_residence_own.click()
        # Доходы
        source_income = self.driver.find_element(*FullFormLocators.SOURCE_INCOME)
        self.driver.execute_script('arguments[0].click();', source_income)
        source_income_employment = self.driver.find_element(*FullFormLocators.SOURCE_INCOME_EMPLOYMENT)
        source_income_employment.click()
        employer_name = self.driver.find_element(*FullFormLocators.EMPLOYER_NAME)
        employer_name.send_keys(data_full_form['employer_name'])
        organization_from_list = self.driver.find_element(*FullFormLocators.ORGANIZATION_FROM_LIST)
        self.driver.execute_script('arguments[0].click();', organization_from_list)
        years_experience = self.driver.find_element(*FullFormLocators.YEARS_EXPERIENCE)
        years_experience.send_keys(data_full_form['years_experience'])
        months_experience = self.driver.find_element(*FullFormLocators.MONTHS_EXPERIENCE)
        months_experience.send_keys(data_full_form['months_experience'])
        position = self.driver.find_element(*FullFormLocators.POSITION)
        position.send_keys(data_full_form['position'])
        position_level = self.driver.find_element(*FullFormLocators.POSITION_LEVEL)
        self.driver.execute_script('arguments[0].click();', position_level)
        position_level_top_manager = self.driver.find_element(*FullFormLocators.POSITION_LEVEL_TOP_MANAGER)
        position_level_top_manager.click()
        copy_from_legal_address = self.driver.find_element(*FullFormLocators.COPY_FROM_LEGAL_ADDRESS)
        self.driver.execute_script('arguments[0].click();', copy_from_legal_address)
        phone_type = self.driver.find_element(*FullFormLocators.PHONE_TYPE)
        self.driver.execute_script('arguments[0].click();', phone_type)
        client_work_phone = self.driver.find_element(*FullFormLocators.CLIENT_WORK_PHONE)
        client_work_phone.click()
        employer_phone = self.driver.find_element(*FullFormLocators.EMPLOYER_PHONE)
        self.driver.execute_script("arguments[0].value = arguments[1];", employer_phone, data_full_form_phone)
        employer_phone.send_keys(data_full_form_phone, Keys.RETURN)
        self.visibility_of_element_located(*FullFormLocators.MESSAGE_ADDING_PHONE)

    def full_app_next_form(self):
        # Далее
        employer_address = self.driver.find_element(*FullFormLocators.EMPLOYER_ADDRESS)
        full_app_next_btn = self.driver.find_element(*FullFormLocators.FULL_APP_NEXT_BTN)

        if employer_address.get_attribute('value') != '':
            full_app_next_btn.click()
        else:
            time.sleep(2)
            full_app_next_btn.click()

        self.driver.refresh()


