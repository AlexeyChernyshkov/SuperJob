import pytest

from pages.resume_create import *
from pages.main_page import Autorization_customers
from pages.base_page import BasePage
from pages.users import *

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
    resume_auth_create_2.top_button_login().click()

    # Ожидаем открытия окна авторизации
    resume_auth_create_2.wait_text_in_element(button_login_accept, "Войти")

    # Авторизуемся методом из main_pages
    authorization_2 = Autorization_customers(browser)
    authorization_2.login(username, password)

    # Ожидаем переход к экрану создания резюме после авторизации
    resume_auth_create_2.wait_element_to_be_clickable(resume_save_button)

    resume_auth_create_2.birthday().send_keys("15.12.1999")

    """Уперся в клик по чек-боксу
    # resume_auth_create_2.check_box_click(hide_birthday_checkbox)
    resume_auth_create_2.hide_birthday_checkbox().click()
    # resume_auth_create_2.remote_work_checkbox().click()
    # resume_auth_create_2.business_trip_checkbox().click()
    # resume_auth_create_2.relocate_possibility_checkbox().click()
    """

    # Открываем окно добавления фото через кнопку
    resume_auth_create_2.add_photo().click()
    resume_auth_create_2.wait_element_to_be_clickable(add_photo_cancel)
    resume_auth_create_2.add_photo_cancel().click()

    # Открываем окно добавления фото через изображение
    resume_auth_create_2.add_photo_img().click()
    resume_auth_create_2.wait_element_to_be_clickable(add_photo_cancel)
    resume_auth_create_2.add_photo_cancel().click()

    resume_auth_create_2.job_position().send_keys("Тестировщик")
    resume_auth_create_2.wait_text_in_element(job_dropdown, "Тестировщик")
    resume_auth_create_2.salary().send_keys("100000")
    resume_auth_create_2.work_type().click()
    resume_auth_create_2.work_type_dropdown_full().click()

    time.sleep(5)


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
