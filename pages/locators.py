from selenium.webdriver.common.by import By

#  Кнопка входа для авторизации
button_input = (By.XPATH, '//span[@class="_38FKN f-test-link-Vhod"]')

#  Поля логин и пароль
field_username = (By.XPATH, '//input[@name="login"]')
field_password = (By.XPATH, '//input[@name="password"]')
# Кнопка Войти
button_login = (By.XPATH, '//button[@class="_129Bc _1L7ad ejaLn PjivS f-test-button-Vojti _26xin"]')

# Строка поиска
the_search_string = (By.XPATH, '//input[@name="keywords"]')
#  Кнопка Найти в поисковой строке
the_search_button = (By.XPATH, '//button[@title="Найти"]')
# селект в строке поиска
selection_selector = (By.XPATH, '//button[@id="searchByHintSelect-input"]')
#  Кнопка Расширенный поиск у фильтров
button_filter_search = (By.XPATH, '//button[@title="Расширенный поиск"]')
# ---------------------------Страница с резюме в ЛК---------------------------------
create_resume = (By.XPATH, '//*[@id="app"]/div/div[1]/div[5]/div/div[1]/div/div[2]/a[1]/span')

# ---------------------------Страница создания резюме---------------------------------
import_resume = (By.CSS_SELECTOR, '.f-test-button-Import_rezyume')
field_name = By.NAME, 'person.firstName'
field_lastname = (By.NAME, 'person.lastName')
field_birthdate = (By.CSS_SELECTOR, 'input[name="birthDate"]')
calendar_birthday = (By.CSS_SELECTOR, '[class="_1yghA WwHMf _2PlM0"]')
hide_birthday_checkbox = (By.NAME, 'hideBirthday')
add_photo = (By.CSS_SELECTOR, 'span > button> span')
add_photo_img = (By.CSS_SELECTOR, 'span > div img')
town = (By.CSS_SELECTOR, '[name="town.id"]:not(.f-test-block-experience [name="town.id"])')
remove_town = (By.CSS_SELECTOR, ':not(.f-test-block-experience .undefined).undefined > span svg')
remote_work_checkbox = (By.NAME, 'remoteWork')
business_trip_checkbox = (By.NAME, 'businessTrip')
relocate_possibility_checkbox = (By.NAME, 'relocatePossibility')
phone = (By.NAME, 'phone')
email = (By.NAME, 'contacts.email')
add_contacts = (By.CSS_SELECTOR, '.f-test-button-Dobavit_kontakty_socseti')
job_position = (By.NAME, 'position')
salary = (By.NAME, 'salary')
work_type = (By.ID, 'workType.id-input')
volunteer_work = (By.NAME, 'volunteerWork')

# Сохранение резюме
resume_save_button = (By.CSS_SELECTOR, '.f-test-button-Sohranit:not(.f-test-block-experience .f-test-button-Sohranit)')
rule_agreement_checkbox = (By.NAME, 'rulesAgreement')
change_user_agreement_text = (
By.CSS_SELECTOR, '.f-test-pseudolink-Izmenit_usloviya_i_zaprety_na_obrabotku_personalnyh_dannyh')
sign_in_button = (By.CSS_SELECTOR, '.f-test-button-Vojti')  # только у неавторизованного юзера

# Раздел "Опыт работы"
experience_position = (By.NAME, 'experience.position')
experience_company_title = (By.NAME, 'resumeCompany.title')
experience_company_site = (By.NAME, 'resumeCompany.website')
experience_company_town = (By.CSS_SELECTOR, '.f-test-block-experience [name="town.id"]')
experience_company_town_remove = (By.CSS_SELECTOR, '.f-test-block-experience .undefined > span')
experience_company_activity = (By.NAME, 'resumeCompany.description')
experience_start_month = (By.CSS_SELECTOR, '[name="dateStart"] input[name="month"]')
experience_start_year = (By.CSS_SELECTOR, '[name="dateStart"] input[name="year"]')
experience_end_month = (By.CSS_SELECTOR, '[name="dateEnd"] input[name="month"]')
experience_end_year = (By.CSS_SELECTOR, '[name="dateEnd"] input[name="year"]')
experience_still_work = (By.NAME, 'stillWorking')
experience_responsibility = (By.NAME, 'responsibility')
experience_achievements = (By.NAME, 'achievements')
no_work_experience_checkbox = (By.NAME, 'noWorkExperience')
experience_save_button = (By.CSS_SELECTOR, '.f-test-block-experience .f-test-button-Sohranit')

# Раздел с доп. параметрами


# --------------------------Страница поиска вакансий---------------------------------

filter_region = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div[2]/div[2]/div/div/div/div['
                           '3]/div/span/div/div/div/h2')
filter_solary = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div[2]/div[2]/div/div/div/div['
                           '5]/div/span/div/div/div/h2')
filter_type_bet = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div[2]/div[2]/div/div/div/div['
                             '6]/div/span/div/div/div/h2')
filter_publication = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div[2]/div[2]/div/div/div/div['
                                '8]/div/span/div/div/div/h2')
filter_specialization = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div[2]/div[2]/div/div/div/div['
                                   '9]/div/div/span/div/div/div/h2')
filter_employment = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div[2]/div[2]/div/div/div/div['
                               '10]/div/span/div/div/div/h2')
filter_type_vacancy = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div[2]/div[2]/div/div/div/div['
                                 '14]/div/span/div/div/div/h2')
filter_additional_parameters = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div[2]/div[2]/div/div/div/div['
                                          '17]/div/span/div/div/div/h2')

# --------------------------Страница поиска вакансий---------------------------------

filter_region_resume = (By.XPATH, "//span[@class='f-test-clickable-title f-test-clickable-Regiony _1Usdr _1aWiZ _2Lgqw']")
filter_active_applicants_resume = (By.XPATH, "//span[@class='f-test-clickable-title f-test-clickable-Aktivnost_soiskatelej _1Usdr _1aWiZ _2Lgqw']")
filter_specialization_resume = (By.XPATH, "//span[@class='f-test-clickable-title f-test-clickable-Specializacii _1Usdr _1aWiZ _2Lgqw']")
filter_work_experience_resume = (By.XPATH, "//span[@class='f-test-clickable-title f-test-clickable-Opyt_raboty _1Usdr _1aWiZ _2Lgqw']")
filter_age_resume = (By.XPATH, "//span[@class='f-test-clickable-title f-test-clickable-Vozrast _1Usdr _1aWiZ _2Lgqw']")
filter_solary_resume = (By.XPATH, "//span[@class='f-test-clickable-title f-test-clickable-Zarplata _1Usdr _1aWiZ _2Lgqw']")
filter_citizenship_resume = (By.XPATH, "//span[@class='f-test-clickable-title f-test-clickable-Grazhdanstvo _1Usdr _1aWiZ _2Lgqw']")
filter_type_of_congestion_resume = (By.XPATH, "//span[@class='f-test-clickable-title f-test-clickable-Tip_zanyatosti _1Usdr _1aWiZ _2Lgqw']")
filter_language_proficiency_resume = (By.XPATH, "//span[@class='f-test-clickable-title f-test-clickable-Vladenie_in_yazykom _1Usdr _1aWiZ _2Lgqw']")
filter_education_resume = (By.XPATH, "//span[@class='f-test-clickable-title f-test-clickable-Obrazovanie _1Usdr _1aWiZ _2Lgqw']")
filter_driver_license_resume = (By.XPATH, "//span[@class='f-test-clickable-title f-test-clickable-Nalichie_prav _1Usdr _1aWiZ _2Lgqw']")

# --------------------------Страница поиска вакансий---------------------------------

filter_specialization_courses = (By.XPATH,"//span[@class='f-test-clickable-title f-test-clickable-Specializacii _1Usdr _1aWiZ _2Lgqw']" )
filter_form_of_education_courses = (By.XPATH,"//span[@class='f-test-clickable-title f-test-clickable-Format_obucheniya _1Usdr _1aWiZ _2Lgqw']")
filter_complexity_courses = (By.XPATH, "//span[@class='f-test-clickable-title f-test-clickable-Uroven_slozhnosti _1Usdr _1aWiZ _2Lgqw']")
filter_cost_courses = (By.XPATH, "//span[@class='f-test-clickable-title f-test-clickable-Stoimost _1Usdr _1aWiZ _2Lgqw']")
filter_school_courses = (By.XPATH, "//span[@class='f-test-clickable-title f-test-clickable-Shkola _1Usdr _1aWiZ _2Lgqw']")
