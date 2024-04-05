# Тут тест проверки открытия страницы резюме и с фиксацией итогового результата
import time

from pages.detail_resume_page import *
from pages.locators import *


def test_detail_resume(browser):
    resume_detail = DetailPageResume(browser, detail_resume_url)
    resume_detail.open()
    time.sleep(1)
    try:
        # Ожидаем когда страница загрузится и селект станет доступным
        resume_detail.wait_presence_of_element_located(selection_selector)
        resume_detail.select_use().click()
        # Ожидаем отображения необходимого значения селектора
        resume_detail.wait_visibility_of_element_located(select_resume)
        resume_detail.select_resume().click()
        resume_detail.search_string().send_keys('Тестировщик')
        resume_detail.button_search_resume().click()
        # Ожидаем прогрузки страницы для дальнейших действий
        resume_detail.wait_visibility_of_element_located(filter_region)
        resume_detail.search_resume().click()
        # Переход на активное окно
        handles = resume_detail.window_handles()
        resume_detail_window = handles[1]
        resume_detail.switch_to_window(resume_detail_window)

    finally:
        #  фиксация результатов
        resume_detail.save_screenshot('test_detail_resume_page.py')
