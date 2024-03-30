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

    def add_photo_cancel(self):
        return self.find(add_photo_cancel)

    def add_photo_close(self):
        return self.find(add_photo_close)

    def add_photo_upload(self):
        return self.find(add_photo_upload)

    def add_photo_save(self):
        return self.find(add_photo_save)

    def town(self):
        return self.find(town)

    def remove_town(self):
        return self.find(remove_town)

    def town_dropdown(self):
        return self.find(town_dropdown)

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

    def job_dropdown(self):
        return self.find(job_dropdown)

    def salary(self):
        return self.find(salary)

    def work_type(self):
        return self.find(work_type)

    def work_type_dropdown_full(self):
        return self.find(work_type_dropdown_full)

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

    def experience_position(self):
        return self.find(experience_position)

    def experience_position_dropdown(self):
        return self.find(experience_position_dropdown)

    def experience_company_title(self):
        return self.find(experience_company_title)

    def experience_company_title_dropdown(self):
        return self.find(experience_company_title_dropdown)

    def experience_company_site(self):
        return self.find(experience_company_site)

    def experience_company_town(self):
        return self.find(experience_company_town)

    def experience_company_town_dropdown(self):
        return self.find(experience_company_town_dropdown)

    def experience_company_town_remove(self):
        return self.find(experience_company_town_remove)

    def experience_company_activity(self):
        return self.find(experience_company_activity)

    def experience_start_month(self):
        return self.find(experience_start_month)

    def experience_start_month_dropdown(self):
        return self.find(experience_start_month_dropdown)

    def experience_start_year(self):
        return self.find(experience_start_year)

    def experience_start_year_dropdown(self):
        return self.find(experience_start_year_dropdown)

    def experience_end_month(self):
        return self.find(experience_end_month)

    def experience_end_month_dropdown(self):
        return self.find(experience_end_month_dropdown)

    def experience_end_year(self):
        return self.find(experience_end_year)

    def experience_end_year_dropdown(self):
        return self.find(experience_end_year_dropdown)

    def experience_still_work(self):
        return self.find(experience_still_work)

    def experience_still_work_click(self, *args):
        return self.script_click(args)

    def experience_responsibility(self):
        return self.find(experience_responsibility)

    def experience_achievements(self):
        return self.find(experience_achievements)

    def no_work_experience_checkbox(self):
        return self.find(no_work_experience_checkbox)

    def experience_save_button(self):
        return self.find(experience_save_button)



