import time
import allure
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.full_form_locators import FullFormLocators
from data.read_save_data import FullFormData
from selenium.webdriver.support.ui import WebDriverWait as wait


class FullForm(BasePage):

    def filling_required_fields_full_form_passage(self):
        # Заполнение обязательных полей, отправить заявку далее по процессу
        with allure.step('Заполнение обязательных полей на полной анкете'):
            self.filling_required_fields_full_form()
        with allure.step('Отправить заявку далее по процессу с полной анкеты'):
            self.full_app_next_form()

    def filling_required_fields_full_form(self):
        data_full_form = FullFormData('../data/data_full_form.json')
        # Запрашиваемые условия
        self.visibility_of_element_located(*FullFormLocators.CREDIT_TERM)
        credit_term = self.find_element(*FullFormLocators.CREDIT_TERM)
        credit_term.send_keys(data_full_form.credit_term)

        self.element_is_clickable(*FullFormLocators.PURPOSE_CREDIT)
        purpose_credit = self.find_element(*FullFormLocators.PURPOSE_CREDIT)
        self.driver.execute_script('arguments[0].click();', purpose_credit)
        # purpose_credit.click()

        self.element_is_clickable(*FullFormLocators.PURPOSE_CREDIT_CAR)
        purpose_credit_car = self.find_element(*FullFormLocators.PURPOSE_CREDIT_CAR)
        purpose_credit_car.click()
        # Инофрмация по клиенту
        family_status = self.find_element(*FullFormLocators.FAMILY_STATUS)
        self.driver.execute_script('arguments[0].click();', family_status)

        family_status_never_married = self.find_element(*FullFormLocators.FAMILY_STATUS_NEVER_MARRIED)
        family_status_never_married.click()

        children_count = self.find_element(*FullFormLocators.COUNT_CHILDREN)
        children_count.send_keys(data_full_form.children_count)

        depends_count = self.find_element(*FullFormLocators.DEPENDS_COUNT)
        depends_count.send_keys(data_full_form.depends_count)
        # Телефон контактного лица
        phone_contact_person = self.find_element(*FullFormLocators.PHONE_CONTACT_PERSON)
        data_full_form_phone = data_full_form.phone
        self.driver.execute_script("arguments[0].value = arguments[1];", phone_contact_person, data_full_form_phone)
        phone_contact_person.send_keys(data_full_form_phone, Keys.RETURN)
        # Адреса
        reasons_residence = self.find_element(*FullFormLocators.REASONS_RESIDENCE)
        self.driver.execute_script('arguments[0].click();', reasons_residence)
        basis_residence_own = self.find_element(*FullFormLocators.BASIS_RESIDENCE_OWN)
        basis_residence_own.click()
        # Доходы
        source_income = self.find_element(*FullFormLocators.SOURCE_INCOME)
        self.driver.execute_script('arguments[0].click();', source_income)
        source_income_employment = self.find_element(*FullFormLocators.SOURCE_INCOME_EMPLOYMENT)
        source_income_employment.click()

        self.element_is_clickable(*FullFormLocators.PHONE_TYPE)
        phone_type = self.find_element(*FullFormLocators.PHONE_TYPE)
        self.driver.execute_script('arguments[0].click();', phone_type)
        self.element_is_clickable(*FullFormLocators.CLIENT_WORK_PHONE)
        client_work_phone = self.find_element(*FullFormLocators.CLIENT_WORK_PHONE)
        client_work_phone.click()
        employer_phone = self.find_element(*FullFormLocators.EMPLOYER_PHONE)
        self.driver.execute_script("arguments[0].value = arguments[1];", employer_phone, data_full_form_phone)
        employer_phone.send_keys(data_full_form_phone, Keys.RETURN)
        self.driver.save_screenshot("screenshot.png")

        self.not_empty_value(employer_phone)
        employer_name = self.find_element(*FullFormLocators.EMPLOYER_NAME)
        employer_name.send_keys(data_full_form.employer_name)
        organization_from_list = self.find_element(*FullFormLocators.ORGANIZATION_FROM_LIST)
        self.driver.execute_script('arguments[0].click();', organization_from_list)
        years_experience = self.find_element(*FullFormLocators.YEARS_EXPERIENCE)
        years_experience.send_keys(data_full_form.years_experience)
        months_experience = self.find_element(*FullFormLocators.MONTHS_EXPERIENCE)
        months_experience.send_keys(data_full_form.months_experience)
        position = self.find_element(*FullFormLocators.POSITION)
        position.send_keys(data_full_form.position)
        position_level = self.find_element(*FullFormLocators.POSITION_LEVEL)
        self.driver.execute_script('arguments[0].click();', position_level)
        position_level_top_manager = self.find_element(*FullFormLocators.POSITION_LEVEL_TOP_MANAGER)
        position_level_top_manager.click()

        copy_from_legal_address = self.find_element(*FullFormLocators.COPY_FROM_LEGAL_ADDRESS)
        self.driver.execute_script('arguments[0].click();', copy_from_legal_address)

    def full_app_next_form(self):
        # Далее
        employer_address = self.find_element(*FullFormLocators.EMPLOYER_ADDRESS)
        full_app_next_btn = self.find_element(*FullFormLocators.FULL_APP_NEXT_BTN)
        self.not_empty_value(employer_address)
        full_app_next_btn.click()
        self.element_is_not_clickable(*FullFormLocators.FULL_APP_NEXT_BTN)






