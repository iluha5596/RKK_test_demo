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
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    elif browser_name == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield driver
    print("\nquit browser")
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs['driver']
        except KeyError:
            return
        screenshot_path = f"screenshot_{item.name}.png"
        driver.save_screenshot(screenshot_path)
        print(f"\nScreenshot saved as {screenshot_path}")


@pytest.fixture
def base_url(request):
    base_url = request.config.getoption('base_url')

    if base_url == 't1':
        return ['https://stend_1', 'T1']
    elif base_url == 't2':
        return ['https://stend_t2', 'T2']
    elif base_url == 't3':
        return ['https://stend_t3', 'T3']
    elif base_url == 't4':
        return ['https://stend_t4', 'T4']
    elif base_url == 'dev':
        return ['https://stend_dev', 'DEV']
    elif base_url == 'demo':
        return ['https://stend_demo', 'DEMO']
    else:
        raise pytest.UsageError('Укажите base_url пример --base_url=t2')


@pytest.fixture
def path(request):
    path = request.config.getoption('path')

    if path == '77777777':
        return '/p_77777777'
    elif path == 'app':
        return '/p_app'
    elif path == 'tas':
        return '/p_tas'
    else:
        raise pytest.UsageError('Укажите путь, пример --path=77777777')
