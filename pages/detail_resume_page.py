import select

from pages.base_page import BasePage
from pages.locators import *

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

# ужна функция н выбор в селекте нужного значения
    def select_use(self):
        return self.find(selection_selector)

    def test(self):
        return self.find(test)
