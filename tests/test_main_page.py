import pytest

from pages.main_page import *
from pages.locators import *
from selenium.common.exceptions import NoSuchElementException
import os


def test_main_menu_links(browser):
    main_menu_links = MainPageMenu(browser, base_url)
    main_menu_links.open()

    try:
        main_menu_links.wait_visibility_of(main_menu_links.kebab_menu())

        assert main_menu_links.main_menu(find_job), f"Ссылка 'Найти работу' не совпадает"
        assert main_menu_links.main_menu(post_a_resume), f"Ссылка 'Разместить резюме' не совпадает"
        assert main_menu_links.main_menu(find_employees), f"Ссылка 'Найти сотрудников' не совпадает"
        assert main_menu_links.main_menu(post_vacancies), f"Ссылка 'Разместить вакансию' не совпадает"
        assert main_menu_links.main_menu(commercial_at_site), f"Ссылка 'Реклама на сайте' не совпадает"
        assert main_menu_links.main_menu(start_of_a_career), f"Ссылка 'Старт карьеры' не совпадает"
        # assert main_menu_links.main_menu(career_guidance), f"Ссылка 'Профориентация' не совпадает"
        assert main_menu_links.main_menu(course), f"Ссылка 'Курсы' не совпадает"
        assert main_menu_links.main_menu(job_seeker_tips), f"Ссылка 'Советы соискателям' не совпадает"
        assert main_menu_links.main_menu(employer_tips), f"Ссылка 'Советы работодателям' не совпадает"
        assert main_menu_links.main_menu(zarplatomer), f"Ссылка 'Зарплатомер' не совпадает"
        assert main_menu_links.main_menu(news), f"Ссылка 'Новости' не совпадает"
        assert main_menu_links.main_menu(researches), f"Ссылка 'Исследования' не совпадает"
        # assert main_menu_links.main_menu(about), f"Ссылка 'О компании' не совпадает"
        assert main_menu_links.main_menu(work_rules), f"Ссылка 'Правила работы' не совпадает"
        assert main_menu_links.main_menu(sitemap), f"Ссылка 'Карта сайта' не совпадает"
        assert main_menu_links.main_menu(find_job_icon), f"Ссылка 'Поиск работы (иконка)' не совпадает"
        assert main_menu_links.main_menu(find_employees_icon), f"Ссылка 'Поиск сотрудников (иконка)' не совпадает"
        assert main_menu_links.main_menu(production_calendar), f"Ссылка 'Производственный календарь' не совпадает"
    except NoSuchElementException as exc:
        print(exc)
        main_menu_links.close()
        os.system(r'pytest -s -v .\tests\test_main_page.py::test_main_menu_links')






