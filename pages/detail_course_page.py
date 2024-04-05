# Тут содержаться методы для детальной страницы поиска курсов
from pages.base_page import BasePage
from pages.locators import *

detail_courses_url = 'https://www.superjob.ru/'


class DetailPageCourses(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def search_string(self):
        return self.find(the_search_string)

    def button_search_resume(self):
        return self.find(the_search_button)

    def search_clients(self):
        return self.find(courses)

    def select_use(self):
        return self.find(selection_selector)

    def select_resume_clients(self):
        return self.find(select_resume_courses)
