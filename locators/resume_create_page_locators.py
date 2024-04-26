from selenium.webdriver.common.by import By

# Обязательные поля
name_required = (By.CSS_SELECTOR, 'label[for="person.firstName"]+.f-test-formField-error')
birthday_required = (By.CSS_SELECTOR, '.f-test-formField-error.f-test-formField-birthDate')
town_required = (By.CSS_SELECTOR, 'label[for="town.id"]+.f-test-formField-error')
phone_required = (By.CSS_SELECTOR, 'label[for="phone"]+.f-test-formField-error')
email_required = (By.CSS_SELECTOR, 'label[for="contacts.email"]+.f-test-formField-error')
position_required = (By.CSS_SELECTOR, 'label[for="position"]+.f-test-formField-error')

# Поля блока основной информации
import_resume = (By.CSS_SELECTOR, '.f-test-button-Import_rezyume')
field_name = (By.NAME, 'person.firstName')
remove_field_name =(By.CSS_SELECTOR, 'label[for="person.firstName"] .undefined > span ')
field_lastname = (By.NAME, 'person.lastName')
remove_field_lastname = (By.CSS_SELECTOR, 'label[for="person.lastName"] .undefined > span ')
field_birthdate = (By.CSS_SELECTOR, 'input[name="birthDate"]')
calendar_birthday = (By.CSS_SELECTOR, 'label[for="birthDate"] div:nth-child(2) div')
hide_birthday_checkbox = (By.NAME, 'hideBirthday')

add_photo = (By.CSS_SELECTOR, '.f-test-button-Dobavit_foto')
add_photo_img = (By.CSS_SELECTOR, '.f-test-clickable-Dobavit_foto')

add_photo_cancel = (By.CSS_SELECTOR, 'button.f-test-button-Otmenit')
add_photo_close = (By.CSS_SELECTOR, '.f-test-button-close')
add_photo_upload = (By.NAME, 'avatar_upload_field')
add_photo_save = (By.CSS_SELECTOR, '#avatarUpload .f-test-button-Sohranit')

town = (By.CSS_SELECTOR, '[name="town.id"]:not(.f-test-block-experience [name="town.id"])')
town_dropdown = (By.CSS_SELECTOR, '[class*="dropdown-town"] span:nth-child(1) button')
remove_town = (By.CSS_SELECTOR, ':not(.f-test-block-experience .undefined) [data-form-id="RESUME_GENERAL_INFO_FORM"] label[for="town.id"] .undefined > span ')
remote_work_checkbox = (By.NAME, 'remoteWork')
business_trip_checkbox = (By.NAME, 'businessTrip')
relocate_possibility_checkbox = (By.NAME, 'relocatePossibility')
phone = (By.NAME, 'phone')
remove_phone = (By.CSS_SELECTOR, 'label[for="phone"] .undefined > span')
email = (By.NAME, 'contacts.email')
remove_email = (By.CSS_SELECTOR, 'label[for="contacts.email"] .undefined > span')
add_contacts = (By.CSS_SELECTOR, '.f-test-button-Dobavit_kontakty_socseti')
job_position = (By.NAME, 'position')
job_dropdown = (By.CSS_SELECTOR, '[class*="dropdown-position"] span:nth-child(1) button')
remove_job_position = (By.CSS_SELECTOR, 'label[for="position"] .undefined > span')
salary = (By.NAME, 'salary')
work_type = (By.ID, 'workType.id-input')
work_type_dropdown_full = (By.ID, "6")
volunteer_work = (By.NAME, 'volunteerWork')

# Сохранение резюме
resume_save_button = (By.CSS_SELECTOR, '.f-test-button-Sohranit:not(.f-test-block-experience .f-test-button-Sohranit)')
successful_resume_create = (By.ID, 'newResume')
rule_agreement_checkbox = (By.NAME, 'rulesAgreement')
change_user_agreement_text = (By.CSS_SELECTOR, '.f-test-pseudolink-Izmenit_usloviya_i_zaprety_na_obrabotku_personalnyh_dannyh')
sign_in_button = (By.CSS_SELECTOR, '.f-test-button-Vojti')  # только у неавторизованного юзера

# Раздел "Опыт работы"
experience_block = (By.CSS_SELECTOR, '.f-test-block-experience')

experience_position = (By.NAME, 'experience.position')
experience_position_dropdown = (By.CSS_SELECTOR, '[class*="dropdown-experience"] span:nth-child(1) button')

experience_company_title = (By.NAME, 'resumeCompany.title')
experience_company_title_dropdown = (By.CSS_SELECTOR, '[class*="dropdown-resumeCompany"] span:nth-child(1) button')

experience_company_site = (By.NAME, 'resumeCompany.website')

experience_company_town = (By.CSS_SELECTOR, '.f-test-block-experience [name="town.id"]')
experience_company_town_dropdown = (By.CSS_SELECTOR, '[class*="dropdown-town"] span:nth-child(1) button')
experience_company_town_remove = (By.CSS_SELECTOR, '.f-test-block-experience [for="town.id"] .undefined > span')

experience_company_activity = (By.NAME, 'resumeCompany.description')

experience_start_month = (By.CSS_SELECTOR, '[name="dateStart"] input[name="month"]')
experience_start_month_dropdown = (By.CSS_SELECTOR, '[class*="dropdown-month"] span:nth-child(1) button')
experience_start_year = (By.CSS_SELECTOR, '[name="dateStart"] input[name="year"]')
experience_start_year_dropdown = (By.CSS_SELECTOR, '[class*="dropdown-year"] span:nth-child(1) button')

experience_end_month = (By.CSS_SELECTOR, '[name="dateEnd"] input[name="month"]')
experience_end_month_dropdown = (By.CSS_SELECTOR, '[class*="dropdown-month"] span:nth-child(1) button')
experience_end_year = (By.CSS_SELECTOR, '[name="dateEnd"] input[name="year"]')
experience_end_year_dropdown = (By.CSS_SELECTOR, '[class*="dropdown-year"] span:nth-child(1) button')

experience_still_work = (By.ID, 'stillWorking')

experience_responsibility = (By.NAME, 'responsibility')
experience_achievements = (By.NAME, 'achievements')
no_work_experience_checkbox = (By.NAME, 'noWorkExperience')
experience_save_button = (By.CSS_SELECTOR, '.f-test-block-experience .f-test-button-Sohranit')
