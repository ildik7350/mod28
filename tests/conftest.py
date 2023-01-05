import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def get_chrome_options():
    options = Options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1900,1000')
    return options


@pytest.fixture(scope='function')
def web_browser(request, get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
    if request.cls is not None:
        request.cls.driver = driver
    driver.delete_all_cookies()
    yield driver
    driver.close()
