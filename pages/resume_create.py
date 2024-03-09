from pages.base_page import BasePage
from pages.locators import *
from selenium.webdriver.common.by import By


resume_create_url = 'https://www.superjob.ru/resume/create/'



class ResumeCreate(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def import_button(self):
        return self.find(import_resume)

    def name(self):
        return self.find(field_name)

    def last_name(self):
        return self.find(field_lastname)

    def birthday(self):
        return self.find(field_birthdate)

    def calendar_bithday(self):
        return self.find(calendar_birthday)