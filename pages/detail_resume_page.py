# Тут содержаться методы для детальной страницы поиска резюме

from pages.base_page import BasePage
from locators.detail_resume_page_locators import *

detail_resume_url = 'https://russia.superjob.ru/'


class DetailPageResume(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def search_string(self):
        return self.find(the_search_string_resume)

    def button_search_resume(self):
        return self.find(the_search_button)

    def search_resume(self):
        return self.find(resume)

    def select_use(self):
        return self.find(selection_selector)

    def select_resume(self):
        return self.find(select_resume)
