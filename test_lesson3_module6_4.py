from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time
import math

links = ["https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"]

text = ""

class TestLogin:
    def test_authorization(self, browser, wait, load_config):

        login = load_config['login_stepik']
        password = load_config['password_stepik']

        
        link = "https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        auth = browser.find_element(By.ID, "ember33")
        auth.click()

        
        
        login_input = browser.find_element(By.NAME, "login")
        login_input.send_keys(login)

        password_input = browser.find_element(By.NAME, "password")
        password_input.send_keys(password)

        input_enter = browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader")
        input_enter.click()

        # Не должно быть окна Автризации
        wait.until_not(EC.visibility_of_element_located((By.CLASS_NAME, "box")))
        
    
    @pytest.mark.parametrize('test_link', links)
    def test_task(self, browser, wait, test_link):
        
        browser.get(test_link)

        # Обнуляем все надписи если тест был решен неправильно
        try:
            refresh_test = browser.find_element(By.CLASS_NAME, "again-btn.white")
            refresh_test.click()
            time.sleep(2)
            click_okey = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="modal-popup__container"]/footer/button[1]')))
            click_okey.click()
        except:
            pass

        # Решить тест заново
        try:
            browser.find_element(By.CLASS_NAME, "again-btn.white").click()
        except:
            pass

        answer = math.log(int(time.time()))
        input_answer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]')))
        input_answer.send_keys(answer)
        
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))).click()
        
        optional_fidbek = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints.ember-view.lesson__hint"))).text
        global text
        if optional_fidbek != "Correct!":
            text = text+str(optional_fidbek)
        assert optional_fidbek == "Correct!"
        return text

    
    def test_total_answer_input(self, browser, wait):
        global text
        print(text)
        link = "https://stepik.org/lesson/237240/step/5?unit=209628"
        browser.get(link)
        
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]')))

        # Обнуляем все надписи если тест был решен неправильно
        try:
            refresh_test = browser.find_element(By.CLASS_NAME, "again-btn.white")
            refresh_test.click()
            click_okey = browser.find_element(By.XPATH, '//*[@class="modal-popup__container"]/footer/button[1]')
            click_okey.click()
        except:
            pass
            
        input_answer = browser.find_element(By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]')
        input_answer.send_keys(str(text))
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        
        wrap_answer_task = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "again-btn.white")))
        continue_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[href="/lesson/237240/step/6?unit=209628"]')))
        assert continue_button.is_enabled() == True, "Не удалось отправить ответ"
        time.sleep(10)