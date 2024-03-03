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