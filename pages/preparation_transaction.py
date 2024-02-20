from datetime import datetime
import allure
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.preparation_transaction_locators import PreparationTransactionLocators
from selenium.webdriver.common.action_chains import ActionChains
from data.read_save_data import PreparationTransactionData


class PreparationTransaction(BasePage):

    def fill_preparation_transaction_cc_passage_task(self):
        # Выбрать две одинаковые коробки и отправить заявку далее по процессу
        with allure.step('Проход заявки на задачу "Подготовка к сделке"'):
            with allure.step('Выбрать две одинаковые коробки и заполнить по нима данные на задаче "Подготовка к сделке"'):
                self.go_product()
                self.on_box()
                self.add_box_solutions()
                self.click_requisites_box()
                self.filling_details_box_1()
                self.filling_details_box_2()
                self.accept_change_box()
            with allure.step('Выбрать действие "Клиент согласен..." и заполнить id карты'):
                self.click_client_agrees()
                self.fill_id_card()
                self.enter_code_word()
            with allure.step('Отправить заявку далее по процессу с задачи "Подготовка к сделке"'):
                self.preparation_transaction_next_form()

    def __init__(self, driver=None, url=None, timeout=20):
        super().__init__(driver, url, timeout)
        # Получение текущей даты
        today = datetime.now()
        # Форматирование даты в строку
        self.formatted_date = today.strftime("%d.%m.%Y")

    def go_product(self):
        # Переход во вкладку продукт
        self.element_is_clickable(*PreparationTransactionLocators.PRODUCT, timeout=120)
        product = self.find_element(*PreparationTransactionLocators.PRODUCT)
        product.click()

    def on_box(self):
        # Включить услугу коробка
        self.element_is_clickable(*PreparationTransactionLocators.SERVICE_BOX, timeout=60)
        service_box = self.find_element(*PreparationTransactionLocators.SERVICE_BOX)
        service_box.click()

    def add_box_solutions(self):
        # Добавить коробку
        data_preparation_transaction = PreparationTransactionData('data/data_preparation_transaction.json')
        self.visibility_of_element_located(*PreparationTransactionLocators.COUNT_BOX_SOLUTIONS, timeout=60)
        box_solution = self.find_element(*PreparationTransactionLocators.COUNT_BOX_SOLUTIONS)
        box_solution.send_keys(data_preparation_transaction.count_box_solutions)

    def click_requisites_box(self):
        # Перейти в заполнение данных по коробке
        self.element_is_clickable(*PreparationTransactionLocators.REQUISITES_BOX, timeout=60)
        requisites_box = self.find_element(*PreparationTransactionLocators.REQUISITES_BOX)
        requisites_box.click()

    def filling_details_box_1(self):
        # Заполнить данные по первой коробке
        data_preparation_transaction = PreparationTransactionData('data/data_preparation_transaction.json')
        self.visibility_of_element_located(*PreparationTransactionLocators.CONTRACT_NUMBER)
        contract_number = self.find_element(*PreparationTransactionLocators.CONTRACT_NUMBER)
        contract_number.send_keys(data_preparation_transaction.contract_number_box_1)
        contract_data = self.find_element(*PreparationTransactionLocators.CONTRACT_DATA)
        contract_data.send_keys(self.formatted_date)

    def filling_details_box_2(self):
        data_preparation_transaction = PreparationTransactionData('data/data_preparation_transaction.json')
        # Переход во вкладку второй коробки и заполнение данных
        box_two = self.find_element(*PreparationTransactionLocators.BOX_TWO)
        box_two.click()
        self.visibility_of_element_located(*PreparationTransactionLocators.CONTRACT_NUMBER)
        # Заполнение данных по второй коробке
        contract_number = self.find_element(*PreparationTransactionLocators.CONTRACT_NUMBER)
        contract_number.send_keys(data_preparation_transaction.contract_number_box_2)
        contract_data = self.find_element(*PreparationTransactionLocators.CONTRACT_DATA)
        contract_data.send_keys(self.formatted_date)

    def accept_change_box(self):
        # Нажать Принять изменения по кробке
        requisites_box_accept = self.find_element(*PreparationTransactionLocators.REQUISITES_BOX_ACCEPT)
        requisites_box_accept.click()

    def click_client_agrees(self):
        # Кликнуть "Клиент согласен..."
        self.invisibility_of_element_located(*PreparationTransactionLocators.REQUISITES_BOX)
        self.element_is_clickable(*PreparationTransactionLocators.CLIENT_AGREES)
        client_agrees = self.find_element(*PreparationTransactionLocators.CLIENT_AGREES)
        client_agrees.click()

    def fill_id_card(self):
        # Заполнить id карты
        input_id_card = self.find_element(*PreparationTransactionLocators.ID_CARD)
        get_card_status = self.find_element(*PreparationTransactionLocators.GET_CARD_STATUS)

        data_preparation_transaction = PreparationTransactionData('data/data_preparation_transaction.json')
        while self.invisibility_of_element_located(*PreparationTransactionLocators.TIPE_CARD, timeout=5):
            current_index = data_preparation_transaction.current_index
            id_card = data_preparation_transaction.id_card
            fill_id_card = id_card[current_index]
            print(f'id_card= {fill_id_card}, current_index= {current_index}')
            while input_id_card.get_attribute('value'):
                input_id_card.send_keys(Keys.BACKSPACE)
            input_id_card.send_keys(fill_id_card)
            get_card_status.click()
            # Увеличиваем текущий индекс
            data_preparation_transaction.current_index += 1
        # Сохранение индекса в файл data_preparation_transaction_read
        data_preparation_transaction.save_data(data_preparation_transaction.current_index)

    def enter_code_word(self):
        # Заполнить кодовое слово
        data_preparation_transaction = PreparationTransactionData('data/data_preparation_transaction.json')
        self.element_is_clickable(*PreparationTransactionLocators.ENTER_CODEWORD)
        enter_codeword = self.find_element(*PreparationTransactionLocators.ENTER_CODEWORD)
        enter_codeword.click()
        self.visibility_of_element_located(*PreparationTransactionLocators.CODEWORD)
        codeword = self.find_element(*PreparationTransactionLocators.CODEWORD)
        codeword.send_keys(data_preparation_transaction.codeword)
        self.element_is_clickable(*PreparationTransactionLocators.SAVE_CODEWORD)
        save_codeword = self.find_element(*PreparationTransactionLocators.SAVE_CODEWORD)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(save_codeword).click().perform()
        self.invisibility_of_element_located(*PreparationTransactionLocators.SAVE_CODEWORD)

    def preparation_transaction_next_form(self):
        # Нажать Далее
        self.element_is_clickable(*PreparationTransactionLocators.BUTTON_NEXT)
        button_next = self.find_element(*PreparationTransactionLocators.BUTTON_NEXT)
        button_next.click()
        self.element_is_not_clickable(*PreparationTransactionLocators.BUTTON_NEXT)






