from selenium.webdriver.common.by import By


the_search_string_clients = (By.XPATH, '//input[@name="key"]')
filter_region_clients = (By.CSS_SELECTOR, ".f-test-clickable-Regiony")
checkbox_open_vacancy = (By.CSS_SELECTOR, ".f-test-link-Kompanii_s_otkrytymi_vakansiyami")
checkbox_attractive_employer = (By.CSS_SELECTOR, ".f-test-link-Privlekatelnyj_rabotodatel")
checkbox_open_employer = (By.CSS_SELECTOR, ".f-test-link-Otkrytyj_rabotodatel")
vacancy_btn = (By.CSS_SELECTOR, '.f-test-link-Vakansii')