#  Тест на проверку основного функционала на странице поиска вакансий
from pages.search_result_vacancy import *


def test_field_exist(browser):
    search_result = SearchResultVacancy(browser, search_result_vacancy_url)
    search_result.open()
    assert search_result.search_string().is_displayed, f"Строка поиска не найдена"

    assert search_result.search_button().is_displayed, f"Кнопка Найти не найдена"

    assert search_result.title() == "Вакансии", f"Селект Вакансии не найден"

    assert search_result.filter_field_button().is_displayed, f"Кнопка Расширенный поиск не найдена"

    assert search_result.filter_field_region().is_displayed, f"Фильтр по регионам не найден"

    assert search_result.filter_field_solary().is_displayed, f"Фильтр по зарплате не найден"

    assert search_result.filter_field_employment().is_displayed, f"Фильтр по типу ставки не найден"

    assert search_result.filter_field_publication().is_displayed, f"Фильтр по периоду публикации не найден"

    assert search_result.filter_field_specialization().is_displayed, f"Фильтр по специализации не найден"

    assert search_result.filter_field_type_vacancy().is_displayed, f"Фильтр по типу занятости не найден"

    assert search_result.filter_field_type_bet().is_displayed, f"Фильтр по типу вакансии не найден"

    assert search_result.filter_field_additional_parameters().is_displayed, f"Фильтр дополнительные параметры не найден"

