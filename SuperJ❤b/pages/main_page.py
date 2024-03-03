from locators import *
from users import *


# Класс для авторизации пользователем
class Autorization_customers:
    def __init__(self, driver):
        self.field_username = driver.find_element(*field_username)
        self.field_password = driver.find_element(*field_password)
        self.button_login = driver.find_element(*button_login)

    def login(self, field_username: str = '', field_password: str = ''):  # авторизация или вход на страницу
        self.field_username.send_keys(test_user_customers)  # заполнение поля логин
        self.field_password.send_keys(test_password_user)  # заполнение поля пароль
        self.button_login.click()  # нажатие на кнопку Войти


#  Класс для авторизации компанией
class Autorization_ccompany:
    def __init__(self, driver):
        self.field_username = driver.find_element(*field_username)
        self.field_password = driver.find_element(*field_password)
        self.button_login = driver.find_element(*button_login)

    def login(self, field_username: str = '', field_password: str = ''):  # авторизация или вход на страницу
        self.field_username.send_keys(test_user_company_1)  # заполнение поля логин
        self.field_password.send_keys(test_password_user_company)  # заполнение поля пароль
        self.button_login.click()  # нажатие на кнопку Войти
