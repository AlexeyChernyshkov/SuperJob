from pages.base_page import BasePage
from pages.locators import *
from selenium.webdriver.common.by import By


user_resume_url = 'https://www.superjob.ru/user/resume/'

class UserResumes(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def update_resumes_btn(self):
        return self.find(update_resumes_btn)

    def create_resume_btn(self):
        return self.find(create_resume_btn)

    def resume_more_options_kebab(self):
        return self.find(resume_more_options_kebab)

    def vision_change_btn(self):
        return self.find(vision_change_btn)

    def auto_response_checkbox(self):
        return self.find(auto_response_checkbox)

    def auto_response_settings_btn(self):
        return self.find(auto_response_settings_btn)

    def up_automate_btn(self):
        return self.find(up_automate_btn)

    def go_to_search_btn(self):
        return self.find(go_to_search_btn)
