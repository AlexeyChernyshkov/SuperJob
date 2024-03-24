from pages.base_page import BasePage
from pages.locators import *

search_result_resumes_url = 'https://www.superjob.ru/resume/search_resume.html'


class SearchResultResume(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def search_string(self):
        return self.find(the_search_string)

    def search_button(self):
        return self.find(the_search_button)

    def title(self):
        return self.find(selection_selector).text

    def filter_field_button(self):
        return self.find(button_filter_search)

    def filter_field_region(self):
        return self.find(filter_region_resume)

    def filter_active_applicants(self):
        return self.find(filter_active_applicants_resume)

    def filter_specialization(self):
        return self.find(filter_specialization_resume)

    def filter_work_experience(self):
        return self.find(filter_work_experience_resume)

    def filter_age(self):
        return self.find(filter_age_resume)

    def filter_solary(self):
        return self.find(filter_solary_resume)

    def filter_citizenship(self):
        return self.find(filter_citizenship_resume)

    def filter_type_of_congestion(self):
        return self.find(filter_type_of_congestion_resume)

    def filter_language_proficiency(self):
        return self.find(filter_language_proficiency_resume)

    def filter_education(self):
        return self.find(filter_education_resume)

    def filter_driver_license(self):
        return self.find(filter_driver_license_resume)
