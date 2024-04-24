#  Тест на проверку основного функционала на странице поиска резюме
from pages.search_result_resumes import *


def test_field_exist(browser):
    search_result = SearchResultResume(browser, search_result_resumes_url)
    search_result.open()

    assert search_result.search_string().is_displayed, f"Строка поиска не найдена"
    assert search_result.search_button().is_displayed, f"Кнопка Найти не найдена"
    assert search_result.title() == "Резюме", f"Селект Резюме не найден"
    assert search_result.filter_field_button().is_displayed, f"Кнопка Расширенный поиск не найдена"
    assert search_result.filter_field_region().is_displayed, f"Фильтр по регионам не найден"
    assert search_result.filter_active_applicants().is_displayed, f"Фильтр по активности пользователей не найден"
    assert search_result.filter_specialization().is_displayed, f"Фильтр по специализации не найден"
    assert search_result.filter_work_experience().is_displayed, f"Фильтр по опыту работы не найден"
    assert search_result.filter_age().is_displayed, f"Фильтр по возрасту не найден"
    assert search_result.filter_solary().is_displayed, f"Фильтр по зарплате не найден"
    assert search_result.filter_citizenship().is_displayed, f"Фильтр по гражданству не найден"
    assert search_result.filter_type_of_congestion().is_displayed, f"Фильтр по типу занятости не найден"
    assert search_result.filter_language_proficiency().is_displayed, f"Фильтр владения иностранным языком не найден"
    assert search_result.filter_education().is_displayed, f"Фильтр образование не найден"
    assert search_result.filter_driver_license().is_displayed, f"Фильтр наличие водительских прав не найден"

