from pages.base_page import BasePage
from locators.search_result_courses_locators import *
from locators.common_locators import *

search_result_courses_url = 'https://www.superjob.ru/kursy/'


class SearchResultCourses(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def search_string(self):
        return self.find(the_search_string)

    def search_button(self):
        return self.find(the_search_button)

    def title(self):
        return self.find(selection_selector).text

    ''' раздел Фильтров '''

    def filter_specialization(self):
        return self.find(filter_specialization_courses)

    def filter_form_of_education(self):
        return self.find(filter_form_of_education_courses)

    def filter_complexity(self):
        return self.find(filter_complexity_courses)

    def filter_cost(self):
        return self.find(filter_cost_courses)

    def filter_school(self):
        return self.find(filter_school_courses)
