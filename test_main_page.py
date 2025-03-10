import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/"

def test_login_link(browser):
    browser.get(link)
    try:
        login_link = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#login_link")))
    except Exception as e:
        pytest.fail(f'Кнопка "Войти или зарегистрироваться" не найдена на странице. Ошибка: {e}')
    assert login_link.is_displayed(), 'Кнопка "Войти или зарегистрироваться" не отображается на странице'
    