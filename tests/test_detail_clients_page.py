# Тут тест проверки открытия страницы резюме и с фиксацией итогового результата
import time

from pages.detail_client_page import *
from pages.locators import *
from time import sleep

def test_detail_resume(browser):
    clients_detail = DetailPageClients(browser, detail_client_url)
    clients_detail.open()
    time.sleep(1)
    try:

        # Ожидаем когда страница загрузится и селект станет доступным
        clients_detail.wait_visibility_of_element_located(selection_selector)
        clients_detail.select_use().click()

        # Ожидаем отображения необходимого значения селектора
        clients_detail.wait_visibility_of_element_located(select_resume_clients)

        clients_detail.select_resume_clients().click()
        clients_detail.search_string().send_keys('Лаборатория касперского')
        clients_detail.button_search_resume().click()
        time.sleep(1)
        # Ожидаем прогрузки страницы для дальнейших действий
        #clients_detail.wait_visibility_of_element_located(filter_specialization_courses)
        #clients_detail.search_clients().click()
        # Переход на активное окно
        #handles = clients_detail.window_handles()
        #resume_detail_window = handles[1]
        #clients_detail.switch_to_window(resume_detail_window)


    finally:
        #  фиксация результатов
        clients_detail.save_screenshot('test_detail_client_page.py')
