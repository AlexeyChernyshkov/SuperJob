from selenium.webdriver.common.by import By

#  Кнопка входа для авторизации
button_input = (By.XPATH, '//span[@class="nCzP5 _2OAxS _2GSjy FbZAB _1quxI"]')

#  Поля логин и пароль
field_username = (By.XPATH, '//input[@name="login"]')
field_password = (By.XPATH, '//input[@name="password"]')
# Кнопка Войти
button_login = (By.XPATH, '//button[@class="_129Bc _1L7ad ejaLn PjivS f-test-button-Vojti _26xin"]')

#  Кнопка Найти в поисковой строке
the_search_button = (By.XPATH, '//button[@title="Найти"]')






# Страница с резюме в ЛК
create_resume = (By.XPATH, '//*[@id="app"]/div/div[1]/div[5]/div/div[1]/div/div[2]/a[1]/span')

# Страница создания резюме
# import_resume = (By.XPATH, '//*[@id="app"]/div/div[1]/div[5]/div/div/div[1]/div/div[1]/div/div/div[1]/button/div/span')
field_name = By.NAME, 'person.firstName'
field_lastname = (By.NAME, 'person.lastName')
field_birthdate = (By.CSS_SELECTOR, 'input[name="birthDate"]')
calendar_birthday = (By.CSS_SELECTOR, '[class="_1yghA WwHMf _2PlM0"]')


