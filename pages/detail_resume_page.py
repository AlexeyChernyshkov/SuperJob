import select

from pages.base_page import BasePage
from pages.locators import *

detail_resume_url = 'https://russia.superjob.ru/'

class DetailPageResume(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def search_string(self):
        return self.find(the_search_string)

    def button_search_resume(self):
        return self.find(the_search_button)

    def search_resume(self):
        return self.find(search_resume)

# ужна функция н выбор в селекте нужного значения