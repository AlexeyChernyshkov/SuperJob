from pages.base_page import BasePage
from pages.locators import *

detail_vacancy_url = 'https://russia.superjob.ru/'

class DetailPageVacancy(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def search_string(self):
        return self.find(the_search_string)

    def search_vacancy(self):
        return self.find(search_vacancy)

    def button_search_vacancy(self):
        return self.find(the_search_button)

    def otklik_vacancy(self):
        return self.find(otklik_vacancy)

    def button_dizlike(self):
        return self.find(button_dizlike)

    def button_like(self):
        return self.find(button_like)

