from selenium import webdriver
import pytest
import json
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="session")
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('config.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config

@pytest.fixture(scope="class")
def browser(request):
    with webdriver.Chrome() as browser:
        browser.implicitly_wait(5) # искать каждый элемент в течение 'n' секунд
        yield browser

# Ожидаем пока какой-либо элемент станет видимым 'n' секунд
@pytest.fixture(scope="function")
def wait(browser):
    return WebDriverWait(browser, 10)
