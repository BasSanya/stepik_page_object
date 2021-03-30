import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose site language. For example "en" or "fr"')

@pytest.fixture(scope="function")
def browser(request):
    site_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': site_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()