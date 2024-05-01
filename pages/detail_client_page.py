# Тут содержаться методы для детальной страницы поиска компаний
from pages.base_page import BasePage
from locators.detail_client_page_locators import *

detail_client_url = 'https://www.superjob.ru/'


class DetailPageClients(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def search_string(self):
        return self.find(the_search_string_clients)

    def button_search_resume(self):
        return self.find(the_search_button)

    def search_clients(self):
        return self.find(courses)

    def select_use(self):
        return self.find(selection_selector_client)

    def select_resume_clients(self):
        return self.find(select_resume_clients)

    def vacancy_btn(self):
        return self.find(vacancy_btn)
