from pages.search_result_vacancy import *


def test_field_exist(browser):
    search_result = SearchResult(browser, search_result_vacancy_url)
    search_result.open()
    assert search_result.search_string().is_displayed
    print('Найдено Строка поиска')
    assert search_result.search_button().is_displayed
    print('Найдена Кнопка поиска')
    assert search_result.title() == "Вакансии"
    print('Найдено Вакансии')
    assert search_result.filter_field_button().is_displayed
    print('Найдена кнопка расширенного поиска')
    assert search_result.filter_field_region().is_displayed
    print('Найден фильтр')
    assert search_result.filter_field_solary().is_displayed
    print('Найден фильтр')
    assert search_result.filter_field_employment().is_displayed
    print('Найден фильтр')
    assert search_result.filter_field_publication().is_displayed
    print('Найден фильтр')
    assert search_result.filter_field_specialization().is_displayed
    print('Найден фильтр')
    assert search_result.filter_field_type_vacancy().is_displayed
    print('Найден фильтр')
    assert search_result.filter_field_type_bet().is_displayed
    print('Найден фильтр')
    assert search_result.filter_field_additional_parameters().is_displayed
    print('Найден фильтр')
