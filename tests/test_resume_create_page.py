from pages.resume_create import *


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


def test_resume_completion(browser):
    resume_completion = ResumeCreate(browser, resume_create_url)
    resume_completion.open()
    resume_completion.wait_text_in_element(resume_save_button, "Сохранить")
    resume_completion.name().send_keys("Alexey")
    resume_completion.last_name().send_keys("Chernyshkov")
    resume_completion.birthday().send_keys("15.12.1999")
    # assert resume_completion.remove_town().is_enabled, "not click"
    # resume_completion.remove_town().click()
    time.sleep(5)
