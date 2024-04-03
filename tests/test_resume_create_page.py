import pytest

from pages.resume_create import *
from pages.main_page import Autorization_customers
from pages.base_page import BasePage
from pages.users import *
from selenium.common.exceptions import TimeoutException
from pages.locators import *

import time


# Проходит, только если человек авторизован, иначе кнопки импорта нет
# def test_import_button_exist(browser):
#     resume_create = ResumeCreate(browser, resume_create_url)
#     resume_create.open()
#     # browser.implicitly_wait(5)
#     assert resume_create.import_button().visibility_of_element_located(), f"No import"


# def test_all_fields_exist(browser):
#     resume_create = ResumeCreate(browser, resume_create_url)
#     resume_create.open()
#     assert resume_create.name().is_displayed, f"No name"
#     assert resume_create.last_name().is_displayed, f"No last_name"
#     assert resume_create.birthday().is_displayed, f"No birthday"
#     assert resume_create.calendar_birthday().is_displayed, f"No calendar_birthday "
#     assert resume_create.hide_birthday_checkbox().is_displayed, f"No hide_birthday_checkbox"
#     assert resume_create.add_photo().is_displayed, f"No add_photo"
#     assert resume_create.add_photo_img().is_displayed, f"No add_photo_img"
#     assert resume_create.town().is_displayed, f"No town"
#     assert resume_create.remote_work_checkbox().is_displayed, f"No remote_work_checkbox"
#     assert resume_create.business_trip_checkbox().is_displayed, f"No business_trip_checkbox"
#     assert resume_create.relocate_possibility_checkbox().is_displayed, f"No relocate_possibility_checkbox"
#     assert resume_create.phone().is_displayed, f"No phone"
#     assert resume_create.email().is_displayed, f"No email"
#     assert resume_create.add_contacts().is_displayed, f"No add_contacts"
#     assert resume_create.job_position().is_displayed, f"No job_position"
#     assert resume_create.salary().is_displayed, f"No salary"
#     assert resume_create.work_type().is_displayed, f"No work_type"
#     assert resume_create.volunteer_work().is_displayed, f"No volunteer_work"
#     assert resume_create.resume_save_button().is_displayed, f"No resume_save_button"
#     assert resume_create.rule_agreement_checkbox().is_displayed, f"No rule_agreement_checkbox"
#     assert resume_create.change_user_agreement_text().is_displayed, f"No change_user_agreement_text"
#     # assert resume_create.sign_in_button().is_displayed, f"No sign_in_button"

# @pytest.mark.parametrize('username, password', [(test_user_customers, test_password_user)])
# def test_resume_create_with_authorization_required_fields_only(browser, username, password):
#     resume_auth_create_1 = ResumeCreate(browser, resume_create_url)
#     resume_auth_create_1.open()
#     resume_auth_create_1.top_button_login().click()
#
#     # Ожидаем открытия окна авторизации
#     resume_auth_create_1.wait_text_in_element(button_login_accept, "Войти")
#
#     # Авторизуемся методом из main_pages
#     authorization_1 = Autorization_customers(browser)
#     authorization_1.login(username, password)
#
#     # Ожидаем переход к экрану создания резюме после авторизации
#     resume_auth_create_1.wait_text_in_element(resume_save_button, "Сохранить")
#
#     resume_auth_create_1.job_position().send_keys("Тестировщик")
#     resume_auth_create_1.wait_text_in_element(job_dropdown, "Тестировщик")
#     resume_auth_create_1.job_dropdown().click()
#     # resume_auth_create.resume_save_button().click()

@pytest.mark.parametrize('username, password', [(test_user_customers, test_password_user)])
def test_resume_create_with_authorization_all_fields(browser, username, password):
    resume_auth_create_2 = ResumeCreate(browser, resume_create_url)
    resume_auth_create_2.open()

    try:
        resume_auth_create_2.top_button_login().click()

        # Ожидаем открытия окна авторизации
        resume_auth_create_2.wait_text_in_element(button_login_accept, "Войти")

        # Авторизуемся методом из main_pages
        authorization_2 = Autorization_customers(browser)
        authorization_2.login(username, password)

        # Ожидаем переход к экрану создания резюме после авторизации, проверкой кликабельности элемента
        resume_auth_create_2.wait_element_to_be_clickable(import_resume)

        # Открываем окно добавления фото через изображение
        resume_auth_create_2.add_photo_img().click()
        resume_auth_create_2.wait_element_to_be_clickable(add_photo_cancel)  # Ожидаем открытия окна загрузки фото
        # Загружаем фото
        resume_auth_create_2.add_photo_upload().send_keys("D:/Тестирование ПО/TOP_Diplom/tests/Djamal_ava.jpg")
        resume_auth_create_2.wait_element_to_be_clickable(add_photo_save)
        resume_auth_create_2.add_photo_save().click()

        # Заполнение основных незаполненных полей
        resume_auth_create_2.last_name().send_keys("Test-last-name")
        resume_auth_create_2.birthday().send_keys("15.12.1999")
        if resume_auth_create_2.get_value(town) != "":
            resume_auth_create_2.remove_town().click()
        resume_auth_create_2.town().send_keys("Барнаул")
        resume_auth_create_2.wait_text_in_element(town_dropdown, "Барнаул")
        resume_auth_create_2.town_dropdown().click()
        resume_auth_create_2.job_position().send_keys("Тестировщик")
        resume_auth_create_2.wait_text_in_element(job_dropdown, "Тестировщик")
        resume_auth_create_2.salary().send_keys("100000")
        resume_auth_create_2.work_type().click()
        resume_auth_create_2.work_type_dropdown_full().click()
    finally:
        resume_auth_create_2.save_screenshot("file_1")

    """Заполнение блока опыта работы"""
    try:
        # Должность
        resume_auth_create_2.experience_position().send_keys("QA-менеджер")
        resume_auth_create_2.wait_text_in_element(experience_position_dropdown, "QA-менеджер")
        resume_auth_create_2.experience_position_dropdown().click()
        # Название компании
        resume_auth_create_2.experience_company_title().send_keys("QA-менеджер")
        resume_auth_create_2.wait_text_in_element(experience_company_title_dropdown, "QA-менеджер")
        resume_auth_create_2.experience_company_title_dropdown().click()
        # Сайт компании
        resume_auth_create_2.experience_company_site().send_keys("https://www.sibirix.ru/")
        # Город
        resume_auth_create_2.experience_company_town_remove().click()
        resume_auth_create_2.experience_company_town().send_keys("Барнаул")
        resume_auth_create_2.wait_text_in_element(experience_company_town_dropdown, "Барнаул")
        resume_auth_create_2.experience_company_town_dropdown().click()
        # Сфера
        resume_auth_create_2.experience_company_activity().send_keys("Разработка сайтов")
        # Начало работы
        resume_auth_create_2.experience_start_month().send_keys("Июль")
        resume_auth_create_2.wait_text_in_element(experience_start_month_dropdown, "Июль")
        resume_auth_create_2.experience_start_month_dropdown().click()

        resume_auth_create_2.experience_start_year().send_keys("2023")
        resume_auth_create_2.wait_text_in_element(experience_start_year_dropdown, "2023")
        resume_auth_create_2.experience_start_year_dropdown().click()
        # Окончание работы
        resume_auth_create_2.experience_end_month().send_keys("Март")
        resume_auth_create_2.wait_text_in_element(experience_end_month_dropdown, "Март")
        resume_auth_create_2.experience_end_month_dropdown().click()

        resume_auth_create_2.experience_end_year().send_keys("2024")
        resume_auth_create_2.wait_text_in_element(experience_end_year_dropdown, "2024")
        resume_auth_create_2.experience_end_year_dropdown().click()

        # Работа по настоящее время
        resume_auth_create_2.script_click(resume_auth_create_2.experience_still_work())
        assert not resume_auth_create_2.experience_end_month().is_enabled(), "not enabled"
        assert not resume_auth_create_2.experience_end_year().is_enabled(), "not enabled"

        # Доп поля
        resume_auth_create_2.experience_responsibility().send_keys("Тестирование")
        resume_auth_create_2.experience_achievements().send_keys("Нашел много дефектов")

        resume_auth_create_2.script_scroll(resume_auth_create_2.salary())
    finally:
        resume_auth_create_2.save_screenshot("file_2")

    # try:
    #     resume_auth_create_2.resume_save_button().click()
    #     resume_auth_create_2.wait_url_matches('www.superjob.ru/user/resume/')
    #
    # finally:
    #     resume_auth_create_2.save_screenshot('file_3')

# def test_resume_completion(browser):
#     resume_completion = ResumeCreate(browser, resume_create_url)
#     resume_completion.open()
#     resume_completion.wait_text_in_element(resume_save_button, "Сохранить")
#     resume_completion.name().send_keys("Alexey")
#     resume_completion.last_name().send_keys("Chernyshkov")
#     resume_completion.birthday().send_keys("15.12.1999")
#     # assert resume_completion.remove_town().is_enabled, "not click"
#     resume_completion.remove_town().click()
#     resume_completion.town().send_keys("Барнаул")
#     resume_completion.wait_text_in_element(town_dropdown, "Барнаул")
#     resume_completion.town_dropdown().click()
#     time.sleep(1)
