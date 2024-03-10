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

    def calendar_birthday(self):
        return self.find(calendar_birthday)

    def hide_birthday_checkbox(self):
        return self.find(hide_birthday_checkbox)

    def add_photo(self):
        return self.find(add_photo)

    def add_photo_img(self):
        return self.find(add_photo_img)

    def town(self):
        return self.find(town)

    def remote_work_checkbox(self):
        return self.find(remote_work_checkbox)

    def business_trip_checkbox(self):
        return self.find(business_trip_checkbox)

    def relocate_possibility_checkbox(self):
        return self.find(relocate_possibility_checkbox)

    def phone(self):
        return self.find(phone)

    def email(self):
        return self.find(email)

    def add_contacts(self):
        return self.find(add_contacts)

    def job_position(self):
        return self.find(job_position)

    def salary(self):
        return self.find(salary)

    def work_type(self):
        return self.find(work_type)

    def volunteer_work(self):
        return self.find(volunteer_work)

    def resume_save_button(self):
        return self.find(resume_save_button)

    def rule_agreement_checkbox(self):
        return self.find(rule_agreement_checkbox)

    def change_user_agreement_text(self):
        return self.find(change_user_agreement_text)

    def sign_in_button(self):
        return self.find(sign_in_button)
