# Тут тест проверки открытия страницы резюме и с фиксацией итогового результата
import time

from pages.detail_course_page import *
from pages.locators import *
from time import sleep

def test_detail_resume(browser):
    courses_detail = DetailPageCourses(browser, detail_courses_url)
    courses_detail.open()
    time.sleep(1)
    try:

        # Ожидаем когда страница загрузится и селект станет доступным
        courses_detail.wait_visibility_of_element_located(selection_selector)
        courses_detail.select_use().click()

        # Ожидаем отображения необходимого значения селектора
        courses_detail.wait_visibility_of_element_located(select_resume_clients)

        courses_detail.select_resume_clients().click()
        courses_detail.search_string().send_keys('тестировщик')
        courses_detail.button_search_resume().click()
        time.sleep(1)
        # Ожидаем прогрузки страницы для дальнейших действий
        courses_detail.wait_visibility_of_element_located(filter_specialization_courses)
        courses_detail.search_clients().click()
        # Переход на активное окно
        handles = courses_detail.window_handles()
        resume_detail_window = handles[1]
        courses_detail.switch_to_window(resume_detail_window)

    finally:
        #  фиксация результатов
        courses_detail.save_screenshot('test_detail_courses_page.py')
