from selenium.webdriver.common.by import By

#  Кнопка входа для авторизации
button_input = (By.XPATH, '//span[@class="nCzP5 _2OAxS _2GSjy FbZAB _1quxI"]')

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


# ---------------------------Страница с резюме в ЛК---------------------------------
create_resume = (By.XPATH, '//*[@id="app"]/div/div[1]/div[5]/div/div[1]/div/div[2]/a[1]/span')

# Страница создания резюме
import_resume = (By.XPATH, '//*[@id="app"]/div/div[1]/div[5]/div/div/div[1]/div/div[1]/div/div/div[1]/button/div/span')
field_name = By.NAME, 'person.firstName'
field_lastname = (By.NAME, 'person.lastName')
field_birthdate = (By.CSS_SELECTOR, 'input[name="birthDate"]')
calendar_birthday = (By.CSS_SELECTOR, '[class="_1yghA WwHMf _2PlM0"]')

# --------------------------Страница поиска вакансий---------------------------------
button_filter_search = (By.XPATH, '//button[@title="Расширенный поиск"]')
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