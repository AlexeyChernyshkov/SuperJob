#  Тест на проверку основного функционала на странице поиска компаний
from pages.search_result_clients import *


def test_field_exist(browser):
    search_result = SearchResultClients(browser, search_result_clients_url)
    search_result.open()

    assert search_result.search_string().is_displayed, f"Строка поиска не найдена"
    assert search_result.search_button().is_displayed, f"Кнопка Найти не найдена"
    assert search_result.title() == "Компании", f"Селект Компании не найден"
    assert search_result.filter_field_button().is_displayed, f"Кнопка расширенный поиск не найдена"
    assert search_result.filter_field_region().is_displayed, f"Фильтр по региону не найден"
    assert search_result.filter_checkbox_1().is_displayed, f"Чекбокс компаний с открытыми вакансиями не найден"
    assert search_result.filter_checkbox_2().is_displayed, f"Чекбокс привлекательный работодатель не найден"
    assert search_result.filter_checkbox_3().is_displayed, f"Чекбокс открытый работодатель не найден"
