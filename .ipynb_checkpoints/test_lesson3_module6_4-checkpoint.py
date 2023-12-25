from selenium import webdriver
from selenium.webdriver.common.by import By
# from conftest import load_config
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time

class TestLogin:
    def test_authorization(self, browser, wait, load_config):

        link = "https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        auth = browser.find_element(By.ID, "ember33")
        auth.click()

        login = load_config['login_stepik']
        password = load_config['password_stepik']
        
        login_input = browser.find_element(By.NAME, "login")
        login_input.send_keys(login)

        password_input = browser.find_element(By.NAME, "password")
        password_input.send_keys(password)

        input_enter = browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader")
        input_enter.click()

        wait.until_not(EC.visibility_of_element_located((By.CLASS_NAME, "box")))

        # time.sleep(2)
        # with pytest.raises(NoSuchElementException):
        #     auth_window = browser.find_element(By.CLASS_NAME, "box")
        #     pytest.fail("Не должно быть окна Автризации")
        time.sleep(10)