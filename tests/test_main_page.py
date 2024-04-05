import pytest

from pages.main_page import *
from pages.users import *
from pages.locators import *
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def test(browser):
    test = MainPageMenu(browser, base_url)
    test.open()

    test.implicitly_wait()
    # test.wait_visibility_of_element_located(top_button_login)

    # assert test.main_menu(find_job), f"Ссылка 'Найти работу' не совпадает"
    # assert test.main_menu(post_a_resume), f"Ссылка 'Разместить резюме' не совпадает"
    # assert test.main_menu(find_employees), f"Ссылка 'Найти сотрудников' не совпадает"
    # assert test.main_menu(post_vacancies), f"Ссылка 'Разместить вакансию' не совпадает"
    # # assert test.main_menu(commercial_at_site), f"Ссылка 'Реклама на сайте' не совпадает"
    # assert test.main_menu(start_of_a_career), f"Ссылка 'Старт карьеры' не совпадает"
    # # assert test.main_menu(career_guidance), f"Ссылка 'Профориентация' не совпадает"
    # assert test.main_menu(course), f"Ссылка 'Курсы' не совпадает"
    # assert test.main_menu(job_seeker_tips), f"Ссылка 'Советы соискателям' не совпадает"
    # assert test.main_menu(employer_tips), f"Ссылка 'Советы работодателям' не совпадает"
    # assert test.main_menu(zarplatomer), f"Ссылка 'Зарплатомер' не совпадает"
    # # assert test.main_menu(news), f"Ссылка 'Новости' не совпадает"
    # assert test.main_menu(researches), f"Ссылка 'Исследования' не совпадает"
    # # assert test.main_menu(about), f"Ссылка 'О компании' не совпадает"
    # assert test.main_menu(work_rules), f"Ссылка 'Правила работы' не совпадает"
    # assert test.main_menu(sitemap), f"Ссылка 'Карта сайта' не совпадает"
    # assert test.main_menu(find_job_icon), f"Ссылка 'Поиск работы (иконка)' не совпадает"
    # assert test.main_menu(find_employees_icon), f"Ссылка 'Поиск сотрудников (иконка)' не совпадает"
    # assert test.main_menu(production_calendar), f"Ссылка 'Производственный календарь' не совпадает"






