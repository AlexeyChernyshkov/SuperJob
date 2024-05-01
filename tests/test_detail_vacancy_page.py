# Тут тест проверки открытия страницы вакансии и с фиксацией итогового результата

from pages.detail_vacancy_page import *
from locators.detail_vacancy_page_locators import *

def test_detail_vacancy(browser):
    vacancy_detail = DetailPageVacancy(browser, detail_vacancy_url)
    vacancy_detail.open()

    try:
        # Заполняем поисковую строку
        vacancy_detail.search_string().send_keys('Python')
        vacancy_detail.button_search_vacancy().click()

        # Ожидаем прогрузки страницы для дальнейших действий
        vacancy_detail.wait_presence_of_element_located(filter_region)
        vacancy_detail.vacancy().click()

        # vacancy_detail.wait_visibility_of_element_located(otklik_vacancy)
        # Переход на активную вкладку для фиксации результатов
        handles = vacancy_detail.window_handles()
        resume_detail_window = handles[1]
        vacancy_detail.switch_to_window(resume_detail_window)
    finally:
        # Фиксация результатов
        vacancy_detail.save_screenshot('test_detail_vacancy_page.py')



#app > div > div._1zxix > div._3C7W2 > div > div:nth-child(2) > div._31epc > div._3VMkc._32Kjr > div:nth-child(1) > div > div:nth-child(1) > div > div
