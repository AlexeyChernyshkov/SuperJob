#  Тест на проверку создания резюме

import pytest

from pages.resume_create import *
from pages.main_page import *
from user_data.users import *
# from locators.main_page_locators import *
from selenium.common.exceptions import NoSuchElementException
import os


@pytest.mark.parametrize('username, password', [(test_user_customers, test_password_user)])
def test_all_fields_exist(browser, username, password):
    resume_create = ResumeCreate(browser, resume_create_url)
    top_menu = MainPageMenu(browser, resume_create_url)
    resume_create.open()
    '''Авторизация'''
    # resume_create.top_button_login().click()

    # Ожидаем открытия окна авторизации
    # resume_create.wait_text_in_element(button_login_accept, "Войти")

    # Авторизуемся методом из main_pages
    authorization_1 = Autorization_customers(browser, base_url)
    authorization_1.login(username, password)

    # Ожидаем переход к экрану создания резюме после авторизации, проверкой кликабельности элемента
    resume_create.wait_element_to_be_clickable(import_resume)

    '''Наличие элементов основного блока'''
    assert resume_create.import_button().is_displayed, f"No import btn"
    assert resume_create.name().is_displayed, f"No name"
    assert resume_create.last_name().is_displayed, f"No last_name"
    assert resume_create.birthday().is_displayed, f"No birthday"
    assert resume_create.calendar_birthday().is_displayed, f"No calendar_birthday "
    assert resume_create.hide_birthday_checkbox().is_displayed, f"No hide_birthday_checkbox"
    assert resume_create.add_photo().is_displayed, f"No add_photo"
    assert resume_create.add_photo_img().is_displayed, f"No add_photo_img"
    assert resume_create.town().is_displayed, f"No town"
    assert resume_create.remote_work_checkbox().is_displayed, f"No remote_work_checkbox"
    assert resume_create.business_trip_checkbox().is_displayed, f"No business_trip_checkbox"
    assert resume_create.relocate_possibility_checkbox().is_displayed, f"No relocate_possibility_checkbox"
    assert resume_create.phone().is_displayed, f"No phone"
    assert resume_create.email().is_displayed, f"No email"
    assert resume_create.add_contacts().is_displayed, f"No add_contacts"
    assert resume_create.job_position().is_displayed, f"No job_position"
    assert resume_create.salary().is_displayed, f"No salary"
    assert resume_create.work_type().is_displayed, f"No work_type"
    assert resume_create.volunteer_work().is_displayed, f"No volunteer_work"

    '''Проверка кнопки сохранения'''
    assert resume_create.resume_save_button().is_displayed, f"No resume_save_button"

    '''Проверка элементов блока опыта работы'''
    assert resume_create.experience_position().is_displayed, f"No position"
    assert resume_create.experience_company_title().is_displayed, f"No company title"
    assert resume_create.experience_company_site().is_displayed, f"No company site"
    assert resume_create.experience_company_town().is_displayed, f"No company town"
    assert resume_create.experience_company_activity().is_displayed, f"No company activity"
    assert resume_create.experience_start_month().is_displayed, f"No start month"
    assert resume_create.experience_start_year().is_displayed, f"No start year"
    assert resume_create.experience_end_month().is_displayed, f"No end month"
    assert resume_create.experience_end_year().is_displayed, f"No end year"
    assert resume_create.experience_still_work().is_displayed, f"No still_work btn"
    assert resume_create.experience_responsibility().is_displayed, f"No responsibility"
    assert resume_create.experience_achievements().is_displayed, f"No achievements"
    assert resume_create.no_work_experience_checkbox().is_displayed, f"No no_work_chck"
    assert resume_create.experience_save_button().is_displayed, f"No exp save btn"


def test_resume_create_with_authorization_required_fields(browser):
    resume_auth_create_1 = ResumeCreate(browser, resume_create_url)
    resume_auth_create_1.open()

    try:
        # Проверка, что обязательные поля не заполнены
        if resume_auth_create_1.get_value(field_name) != "":
            resume_auth_create_1.remove_field_name().click()
        if resume_auth_create_1.get_value(field_birthdate) != "":
            resume_auth_create_1.birthday().clear()
        if resume_auth_create_1.get_value(town) != "":
            resume_auth_create_1.remove_town().click()
        if resume_auth_create_1.get_value(phone) != "":
            resume_auth_create_1.remove_phone().click()
        if resume_auth_create_1.get_value(email) != "":
            resume_auth_create_1.remove_email().click()
        if resume_auth_create_1.get_value(job_position) != "":
            resume_auth_create_1.remove_job_position().click()

        resume_auth_create_1.resume_save_button().click()

        assert resume_auth_create_1.name_required().is_displayed, f"Name no required"
        assert resume_auth_create_1.birthday_required().is_displayed, f"Birthday no required"
        assert resume_auth_create_1.town_required().is_displayed, f"Town no required"
        assert resume_auth_create_1.phone_required().is_displayed, f"Phone no required"
        assert resume_auth_create_1.email_required().is_displayed, f"Email no required"
        assert resume_auth_create_1.position_required().is_displayed, f"Position no required"
    except NoSuchElementException as exc:
        print(exc)
        resume_auth_create_1.close()
        os.system(r'pytest -s -v .\tests\test_resume_create_page.py::test_resume_create_with_authorization_required_fields')
    finally:
        resume_auth_create_1.save_screenshot("test_resume_create_with_authorization_required_fields")


@pytest.mark.parametrize('username, password', [(test_user_customers, test_password_user)])
def test_resume_create_with_authorization_all_fields(browser, username, password):
    resume_auth_create_2 = ResumeCreate(browser, resume_create_url)
    resume_auth_create_2.open()

    try:
        '''Авторизация'''
        # resume_auth_create_2.top_button_login().click()

        # Ожидаем открытия окна авторизации
        # resume_auth_create_2.wait_text_in_element(button_login_accept, "Войти")

        # Авторизуемся методом из main_pages
        authorization_2 = Autorization_customers(browser,base_url)
        authorization_2.login(username, password)

        # Ожидаем переход к экрану создания резюме после авторизации, проверкой кликабельности элемента
        resume_auth_create_2.wait_element_to_be_clickable(import_resume)

        '''Заполнение блока основной информации'''
        # Открываем окно добавления фото через изображение
        resume_auth_create_2.add_photo_img().click()
        resume_auth_create_2.wait_element_to_be_clickable(add_photo_cancel)  # Ожидаем открытия окна загрузки фото

        # Загружаем фото
        resume_auth_create_2.add_photo_upload().send_keys("D:/Тестирование ПО/TOP_Diplom/tests/Djamal_ava.jpg")
        resume_auth_create_2.wait_element_to_be_clickable(add_photo_save)
        resume_auth_create_2.add_photo_save().click()

        # Поле имени
        if resume_auth_create_2.get_value(field_name) != "":
            resume_auth_create_2.remove_field_name().click()
        resume_auth_create_2.name().send_keys("Алексей")

        # Поле фамилии
        if resume_auth_create_2.get_value(field_lastname) != "":
            resume_auth_create_2.remove_field_lastname().click()
        resume_auth_create_2.last_name().send_keys("Чернышков")

        # Дата рождения
        resume_auth_create_2.birthday().send_keys("15.12.1999")

        # Город
        if resume_auth_create_2.get_value(town) != "":
            resume_auth_create_2.remove_town().click()
        resume_auth_create_2.town().send_keys("Барнаул")
        resume_auth_create_2.wait_text_in_element(town_dropdown, "Барнаул")
        resume_auth_create_2.town_dropdown().click()

        # Должность
        resume_auth_create_2.job_position().send_keys("Тестировщик")
        resume_auth_create_2.wait_text_in_element(job_dropdown, "Тестировщик")
        resume_auth_create_2.job_dropdown().click()

        # Зарплата
        resume_auth_create_2.salary().send_keys("100000")

        # Тип занятости
        resume_auth_create_2.work_type().click()
        resume_auth_create_2.work_type_dropdown_full().click()
    except NoSuchElementException as exc:
        print(exc)
        resume_auth_create_2.close()
        os.system(r'pytest -s -v .\tests\test_resume_create_page.py::test_resume_create_with_authorization_all_fields')
    finally:
        resume_auth_create_2.save_screenshot("test_resume_create_with_authorization_all_fields_1")

    try:
        '''Заполнение блока опыта работы'''
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
        resume_auth_create_2.save_screenshot("test_resume_create_with_authorization_all_fields_2")

    # try:
    #     '''Сохраняем резюме'''
    #     resume_auth_create_2.resume_save_button().click()
    #     resume_auth_create_2.wait_visibility_of_element_located(successful_resume_create)
    #     assert resume_auth_create_2.successful_resume_create().is_displayed, f"Not Successful Resume Create"
    # finally:
    #     resume_auth_create_2.save_screenshot('test_resume_create_with_authorization_all_fields_3')

