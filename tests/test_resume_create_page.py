from pages.resume_create import ResumeCreate, resume_create_url
import time


# Проходит, только если человек авторизован, иначе кнопки импорта нет
# def test_import_button_exist(browser):
#     resume_create = ResumeCreate(browser)
#     resume_create.open()
#     # browser.implicitly_wait(5)
#     assert resume_create.import_button().is_displayed()


def test_name_field_exist(browser):
    resume_create = ResumeCreate(browser, resume_create_url)
    resume_create.open()
    assert resume_create.name().is_displayed
    assert resume_create.last_name().is_displayed
    assert resume_create.birthday().is_displayed
    assert resume_create.calendar_bithday().is_displayed




