from selenium.webdriver.common.by import By


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
