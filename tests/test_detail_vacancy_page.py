import pytest

from pages.detail_resume_page import *
from pages.main_page import Autorization_customers
from pages.base_page import BasePage
from pages.users import *
from selenium.common.exceptions import TimeoutException
from pages.locators import *

import time
from selenium.webdriver.common.keys import Keys

@pytest.mark.parametrize('username, password', [(test_user_customers, test_password_user)])
def test_detail_vacancy(browser, username, password):
    resume_auth = DetailPage(browser, detail_vacancy_url)
    resume_auth.open()
    time.sleep(2)
    resume_auth.top_button_login().click()

    # Ожидаем открытия окна авторизации
    resume_auth.wait_text_in_element(button_login_accept, "Войти")

    # Авторизуемся методом из main_pages
    authorization = Autorization_customers(browser)
    authorization.login(username, password)
    time.sleep(3)
    resume_auth.search_string().send_keys('Python')
    resume_auth.button_search_vacancy().click()
    time.sleep(5)
    resume_auth.search_vacancy().click()
    time.sleep(3)
    # Тут надо понять как переключаться между вкладками браузера
    # resume_auth.save_screenshot('vacancy')
    # time.sleep(1)


