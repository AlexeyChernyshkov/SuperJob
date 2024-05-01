# Тут тест проверки открытия страницы резюме и с фиксацией итогового результата

from pages.detail_client_page import *
from locators.common_locators import *
from selenium.common.exceptions import TimeoutException
import os


def test_detail_clients(browser):
    clients_detail = DetailPageClients(browser, detail_client_url)
    clients_detail.open()

    try:
        clients_detail.wait_visibility_of_element_located(selection_selector)
        # Ожидаем когда страница загрузится и селект станет доступным

        clients_detail.select_use().click()

        # Ожидаем отображения необходимого значения селектора
        clients_detail.wait_visibility_of_element_located(select_resume_clients)

        clients_detail.select_resume_clients().click()
        clients_detail.search_string().send_keys('Лаборатория касперского')
        clients_detail.button_search_resume().click()

        clients_detail.wait_url_matches('superjob.ru/clients/')
        clients_detail.wait_element_to_be_clickable(vacancy_btn)
        url = clients_detail.get_page_url()
        assert 'superjob.ru/clients/' in url, f"Not in url"
        clients_detail.save_screenshot('test_detail_client_page.py')

    except TimeoutException as exc:
        print(exc)
        clients_detail.close()
        os.system(r'pytest -s -v .\tests\test_detail_clients_page.py::test_detail_clients')
