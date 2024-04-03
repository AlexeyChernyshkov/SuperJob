import pytest

from pages.detail_resume_page import *
from pages.main_page import Autorization_customers
from pages.base_page import BasePage
from pages.users import *
from selenium.common.exceptions import TimeoutException
from pages.locators import *

import time
from selenium.webdriver.common.keys import Keys


def test_detail_resume(browser):
    resume_detail = DetailPageResume(browser, detail_resume_url)
    resume_detail.open()

    try:
        resume_detail.wait_element_to_be_clickable(selection_selector)
        resume_detail.select_use().click()
        resume_detail.wait_visibility_of_element_located(test)

        resume_detail.test().click()

        resume_detail.search_string().send_keys('Тестировщик')
        resume_detail.button_search_resume().click()
        resume_detail.wait_visibility_of_element_located(filter_region)
        resume_detail.search_resume().click()

        handles = resume_detail.window_handles()
        resume_detail_window = handles[1]
        resume_detail.switch_to_window(resume_detail_window)



    finally:
        resume_detail.save_screenshot('test_detail_resume_page.py')



