from pages.base_page import BasePage
from pages.locators import *

search_result_vacancy_url = 'https://www.superjob.ru/vacancy/search/'


class SearchResult(BasePage):

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
        return self.find(filter_region)

    def filter_field_solary(self):
        return self.find(filter_solary)

    def filter_field_type_bet(self):
        return self.find(filter_type_bet)

    def filter_field_publication(self):
        return self.find(filter_publication)

    def filter_field_publication(self):
        return self.find(filter_publication)

    def filter_field_specialization(self):
        return self.find(filter_specialization)

    def filter_field_employment(self):
        return self.find(filter_employment)

    def filter_field_type_vacancy(self):
        return self.find(filter_type_vacancy)

    def filter_field_additional_parameters(self):
        return self.find(filter_additional_parameters)

