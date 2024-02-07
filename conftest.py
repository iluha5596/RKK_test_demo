import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose name browser chrome or firefox')
    parser.addoption('--base_url',
                     help="Specify the base URL for the test t1/t2/t3...")
    parser.addoption('--path',
                     help='Specify client cft id')


@pytest.fixture(scope='function')
def driver(request):
    browser_name = request.config.getoption('browser_name')

    if browser_name == 'chrome':
        options = ChromeOptions()
        # options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    elif browser_name == 'firefox':
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield driver
    print("\nquit browser")
    driver.quit()


@pytest.fixture
def base_url(request):
    base_url = request.config.getoption('base_url')

    if base_url == 't1':
        return ['https://rkk-t1.dev.zenit.ru', 'T1']
    elif base_url == 't2':
        return 'https://rkk-t2.dev.zenit.ru'
    elif base_url == 't4':
        return 'https://rkk-t4.dev.zenit.ru'
    elif base_url == 'dev':
        return 'https://rkk.dev.zenit.ru'
    elif base_url == 'demo':
        return ['https://rkk-demo.dev.zenit.ru', 'DEMO']
    # Если значение base_url не соответствует ни одному условию, вернёт текст ошибки
    else:
        raise pytest.UsageError('Укажите base_url пример --base_url=t2')


@pytest.fixture
def path(request):
    path = request.config.getoption('path')

    if path == '149551799240':
        return '/xbpm/runtime/applications/ru.unitarius.zenit/znt-lfr-objects/1.0.0/actions/createRequest?actionParams={"crmClientId":"af56adf","cftClientId":"149551799240"}'
    elif path == '398166901374':
        return '/xbpm/runtime/applications/ru.unitarius.zenit/znt-lfr-objects/1.0.0/actions/createRequest?actionParams={"crmClientId":"sdfa54a5","cftClientId":"149551799240"}'
    elif path == 'applications':
        return '/xbpm/runtime/applications/ru.unitarius.zenit/znt-lfr-objects/1.0.0/forms/appFormRequestsMyForm'
    elif path == 'tasks':
        return '/xbpm/runtime/applications/ru.unitarius.zenit/znt-lfr-objects/1.0.0/forms/appFormTasksMyForm'
    else:
        raise pytest.UsageError('Укажите путь, пример --path=149551799240')
