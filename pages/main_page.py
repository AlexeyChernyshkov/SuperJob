from locators.main_page_locators import *
from pages.base_page import BasePage

base_url = 'https://www.superjob.ru/'


# Класс для авторизации пользователем
class Autorization_customers(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def open_login_page(self):
        self.browser.find_element(*top_button_login).click()
        self.wait_text_in_element(button_login_accept, "Войти")

    def login(self, username: str = '', password: str = ''):  # авторизация или вход на страницу
        self.browser.find_element(*field_username).send_keys(username)
        self.browser.find_element(*field_password).send_keys(password)
        self.browser.find_element(*button_login_accept).click()


class MainPageMenu(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def kebab_menu(self):
        return self.find(kebab_menu)

    def main_menu(self, element):
        self.kebab_menu().click()
        return self.compare_url(element)

