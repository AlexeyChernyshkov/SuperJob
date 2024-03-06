import sys

from .base_page import BasePage
# from config import *
from .locators import *
from .users import *


class ResumeCreate(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

        self.name = self.browser.find_element(field_name)
        self.lastname = self.browser.find_element(field_lastname)
        self.birthdate = self.browser.find_element(field_birthdate)

    def field_input(self):
        self.name.send_keys("TestName")
        self.lastname.send_keys("TestLastname")
