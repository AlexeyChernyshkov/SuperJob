from locators.main_page_locators import *
from user_data.users import *
from pages.base_page import BasePage

# resume_create_url = 'https://www.superjob.ru/resume/create/'
base_url = 'https://www.superjob.ru/'


# Класс для авторизации пользователем
class Autorization_customers(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.top_button_login = browser.top_button_login
        self.field_username = browser.find_element(*field_username)
        self.field_password = browser.find_element(*field_password)
        self.button_login_accept = browser.find_element(*button_login_accept)

    def login(self, field_username: str = '', field_password: str = ''):  # авторизация или вход на страницу
        self.top_button_login.click()
        self.wait_text_in_element(button_login_accept, "Войти")
        self.field_username.send_keys(test_user_customers)  # заполнение поля логин
        self.field_password.send_keys(test_password_user)  # заполнение поля пароль
        self.button_login_accept.click()  # нажатие на кнопку Войти

    def login_with_resumes(self, field_username: str = '', field_password: str = ''):  # авторизация или вход на страницу
        self.top_button_login.click()
        self.wait_text_in_element(button_login_accept, "Войти")
        self.field_username.send_keys(test_user_customers_with_resumes)  # заполнение поля логин
        self.field_password.send_keys(test_password_user_with_resumes)  # заполнение поля пароль
        self.button_login_accept.click()  # нажатие на кнопку Войти


class MainPageMenu(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def kebab_menu(self):
        return self.find(kebab_menu)

    def main_menu(self, element):
        self.kebab_menu().click()
        return self.compare_url(element)



#  Класс для авторизации компанией пока не актуально

# class Autorization_ccompany:
#     def __init__(self, driver):
#         self.field_username = driver.find_element(*field_username)
#         self.field_password = driver.find_element(*field_password)
#         self.button_login_accept = driver.find_element(*button_login_accept)
#
#     def login(self, field_username: str = '', field_password: str = ''):  # авторизация или вход на страницу
#         self.field_username.send_keys(test_user_company_1)  # заполнение поля логин
#         self.field_password.send_keys(test_password_user_company)  # заполнение поля пароль
#         self.button_login_accept.click()  # нажатие на кнопку Войти
