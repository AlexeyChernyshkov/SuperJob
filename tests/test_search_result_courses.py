#  Тест на проверку основного функционала на странице поиска курсов
from pages.search_result_courses import *


def test_field_exist(browser):
    search_result = SearchResultCourses(browser, search_result_courses_url)
    search_result.open()

    assert search_result.search_string().is_displayed, f"Строка поиска не найдена"

    assert search_result.search_button().is_displayed, f"Кнопка Найти не найдена"

    assert search_result.title() == "Курсы", f"Селект Курсы не найден"

    assert search_result.filter_specialization().is_displayed, f"Фильтр по специализации не найден"

    assert search_result.filter_form_of_education().is_displayed, f"Фильтр по формату обучения не найден"

    assert search_result.filter_complexity().is_displayed, f"Фильтр по уровню сложности не найден"

    assert search_result.filter_cost().is_displayed, f"Фильтр по стоимости не найден"

    assert search_result.filter_school().is_displayed, f"Фильтр по школе не найден"
