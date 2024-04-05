from selenium.webdriver.common.by import By

#  Кнопка входа для авторизации
# top_button_login = (By.XPATH, '//span[@class="_38FKN f-test-link-Vhod"]')
top_button_login = (By.CSS_SELECTOR, '.f-test-button-Voĭti')

#  Поля логин и пароль
field_username = (By.XPATH, '//input[@name="login"]')
field_password = (By.XPATH, '//input[@name="password"]')

# Кнопка Войти
# button_login_accept = (By.XPATH, '//button[@class="_129Bc _1L7ad ejaLn PjivS f-test-button-Vojti _26xin"]')
button_login_accept = (By.CSS_SELECTOR, '.f-test-button-Vojti')
notifications = (By.CSS_SELECTOR, 'f-test-button-notifications')
top_account = (By.CSS_SELECTOR, 'f-test-tooltip-Nastrojki_Vyjti')

# ---------------------------Страница с резюме в ЛК---------------------------------
create_resume = (By.XPATH, '//*[@id="app"]/div/div[1]/div[5]/div/div[1]/div/div[2]/a[1]/span')

# --------------------------- Боковое меню------------------------------------------
kebab_menu = (By.CSS_SELECTOR, '.f-test-button-dehaze')
find_job = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Najti_rabotu')
post_a_resume = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Razmestit_rezyume')
find_employees = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Najti_sotrudnikov')
post_vacancies = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Razmestit_vakansiyu')
commercial_at_site = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Reklama_na_sajte')
start_of_a_career = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Start_karery')
career_guidance = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Proforientaciya')
course = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Kursy')
job_seeker_tips = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Sovety_soiskatelyam')
employer_tips = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Sovety_rabotodatelyam')
zarplatomer = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Igra_«Zarplatomer»')
news = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Novosti')
researches = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Issledovaniya')
about = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-O_kompanii')
work_rules = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Pravila_raboty')
sitemap = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Karta_sajta')
find_job_icon = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Poisk_raboty')
find_employees_icon = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Poisk_sotrudnikov')
production_calendar = (By.CSS_SELECTOR, '[role="presentation"] .f-test-link-Proizvodstvennyj_kalendar')

# ---------------------------Страница создания резюме---------------------------------
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


# Строка поиска, у резюме своя строка
the_search_string = (By.XPATH, '//input[@name="keywords"]')
#  Кнопка Найти в поисковой строке
the_search_button = (By.CSS_SELECTOR, '.f-test-button-Najti')
# селект в строке поиска
# selection_selector = (By.CSS_SELECTOR, '.f-test-select-searchByHintSelect')
selection_selector = (By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/form/div[2]/div/div/div[1]/button/div')
#  Кнопка Расширенный поиск у фильтров
button_filter_search = (By.XPATH, '//button[@title="Расширенный поиск"]')

# --------------------------Мои резюме----------------------------------------------

update_resumes_btn = (By.CSS_SELECTOR, '.f-test-button-Obnovit_vse_rezyume')
create_resume_btn = (By.CSS_SELECTOR, 'f-test-button-Sozdat_rezyume')
resume_more_options_kebab = (By.CSS_SELECTOR, '.f-test-resume_card .f-test-button-more_vert')
vision_change_btn = (By.CSS_SELECTOR, '.f-test-resume_card .f-test-clickable-Izmenit')
auto_response_checkbox = (By.CSS_SELECTOR, '[name*="resumeCardAutoResponse"]')
auto_response_settings_btn = (By.CSS_SELECTOR, '.f-test-clickable-Nastroit')
up_automate_btn = (By.CSS_SELECTOR, '.f-test-button-Podnimat_avtomaticheski')
go_to_search_btn = (By.CSS_SELECTOR, '.f-test-button-Perejti_k_poisku')


# --------------------------Страница поиска вакансий---------------------------------

filter_region = (By.CSS_SELECTOR, '.f-test-clickable-Regiony')
filter_solary = (By.CSS_SELECTOR, '.f-test-clickable-Zarplata')
filter_type_bet = (By.CSS_SELECTOR, '.f-test-clickable-Tip_stavki')
filter_publication = (By.CSS_SELECTOR, '.f-test-clickable-Period_publikacii')
filter_specialization = (By.CSS_SELECTOR, '.f-test-clickable-Specializacii')
filter_employment = (By.CSS_SELECTOR, '.f-test-clickable-Tip_zanyatosti')
filter_type_vacancy = (By.CSS_SELECTOR, '.f-test-clickable-Tip_vakansii')
filter_additional_parameters = (By.CSS_SELECTOR, '.f-test-clickable-Dopolnitelnye_parametry')

# --------------------------Страница поиска резюме---------------------------------
# Строка поиска
the_search_string_resume = (By.XPATH, '//input[@name="keywords[0][keys]"]')

filter_region_resume = (By.CSS_SELECTOR, ".f-test-clickable-Regiony")
filter_active_applicants_resume = (By.CSS_SELECTOR, ".f-test-clickable-Aktivnost_soiskatelej")
filter_specialization_resume = (By.CSS_SELECTOR, ".f-test-clickable-Specializacii")
filter_work_experience_resume = (By.CSS_SELECTOR, ".f-test-clickable-Opyt_raboty")
filter_age_resume = (By.CSS_SELECTOR, ".f-test-clickable-Vozrast")
filter_solary_resume = (By.CSS_SELECTOR, ".f-test-clickable-Zarplata")
filter_citizenship_resume = (By.CSS_SELECTOR, ".f-test-clickable-Grazhdanstvo")
filter_type_of_congestion_resume = (By.CSS_SELECTOR, ".f-test-clickable-Tip_zanyatosti")
filter_language_proficiency_resume = (By.CSS_SELECTOR, ".f-test-clickable-Vladenie_in_yazykom")
filter_education_resume = (By.CSS_SELECTOR, ".f-test-clickable-Obrazovanie")
filter_driver_license_resume = (By.CSS_SELECTOR, ".f-test-clickable-Nalichie_prav")

# --------------------------Страница поиска курсы---------------------------------

filter_specialization_courses = (By.CSS_SELECTOR,".f-test-clickable-Specializacii" )
filter_form_of_education_courses = (By.CSS_SELECTOR,".f-test-clickable-Format_obucheniya")
filter_complexity_courses = (By.CSS_SELECTOR, ".f-test-clickable-Uroven_slozhnosti")
filter_cost_courses = (By.CSS_SELECTOR, ".f-test-clickable-Stoimost")
filter_school_courses = (By.CSS_SELECTOR, ".f-test-clickable-Shkola")


# --------------------------Страницв поиска компаний ------------------------------
the_search_string_clients = (By.XPATH, '//input[@name="key"]')
filter_region_clients = (By.CSS_SELECTOR, ".f-test-clickable-Regiony")
checkbox_open_vacancy = (By.CSS_SELECTOR, ".f-test-link-Kompanii_s_otkrytymi_vakansiyami")
checkbox_attractive_employer = (By.CSS_SELECTOR, ".f-test-link-Privlekatelnyj_rabotodatel")
checkbox_open_employer = (By.CSS_SELECTOR, ".f-test-link-Otkrytyj_rabotodatel")

# --------------------------Детальная страница поиска резюме ------------------------------

search_resume = (By.XPATH, '#app .f-test-search-result-item > div:first-child .f-test-link-resume-name')
test = (By.XPATH, '//div[@id="searchByHintSelect-item-1"]')
resume = (By.XPATH, '/html/body/div[2]/div/div[1]/div[4]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/a/div/div[1]/div[1]/span')
# --------------------------Детальная страница поиска вакансии ------------------------------
# search_vacancy = (By.CSS_SELECTOR, '#app .f-test-search-result-item > div:first-child .f-test-vacancy-item')
vacancy = (By.XPATH, '/html/body/div[1]/div/div[1]/div[4]/div/div[2]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div/span/a')
search_vacancy = (By.XPATH, '/html/body/div[1]/div/div[1]/div[4]/div/div[2]/div[1]/div[1]/div/div[1]/div')
otklik_vacancy = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/button')
button_dizlike = (By.CSS_SELECTOR, '.f-test-button-visibility_off')
button_like = (By.XPATH, '//*[@id="app"]/div/div[1]/div[5]/div/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div')




# --------------------------Детальная страница поиска компании ------------------------------



# --------------------------Детальная страница поиска курса ------------------------------
