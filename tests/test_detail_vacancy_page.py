import pytest

from pages.detail_vacancy_page import *
from pages.main_page import Autorization_customers
from pages.base_page import BasePage
from pages.users import *
from selenium.common.exceptions import TimeoutException
from pages.locators import *

import time
from selenium.webdriver.common.keys import Keys


def test_detail_vacancy(browser):
    vacancy_detail = DetailPageVacancy(browser, detail_vacancy_url)
    vacancy_detail.open()

    try:
        # Заполняем поисковую строку
        vacancy_detail.search_string().send_keys('Python')
        vacancy_detail.button_search_vacancy().click()

        vacancy_detail.wait_element_to_be_clickable(search_vacancy)
        vacancy_detail.search_vacancy().click()
        handles = vacancy_detail.window_handles()
        resume_detail_window = handles[1]
        vacancy_detail.switch_to_window(resume_detail_window)
        vacancy_detail.wait_element_to_be_clickable(otklik_vacancy)

    finally:
        vacancy_detail.save_screenshot('vacancy')



#app > div > div._1zxix > div._3C7W2 > div > div:nth-child(2) > div._31epc > div._3VMkc._32Kjr > div:nth-child(1) > div > div:nth-child(1) > div > div
