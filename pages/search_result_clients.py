from pages.base_page import BasePage
from locators.search_result_clients_locators import *
from locators.common_locators import *


search_result_clients_url = 'https://russia.superjob.ru/clients/'

class SearchResultClients(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser,url)

    def search_string(self):
        return self.find(the_search_string_clients)

    def search_button(self):
        return self.find(the_search_button)

    def title(self):
        return self.find(selection_selector).text

    ''' раздел Фильтров '''

    def filter_field_button(self):
        return self.find(button_filter_search)

    def filter_field_region(self):
        return self.find(filter_region_clients)

    def filter_checkbox_1(self):
        return self.find(checkbox_open_vacancy)

    def filter_checkbox_2(self):
        return self.find(checkbox_attractive_employer)

    def filter_checkbox_3(self):
        return self.find(checkbox_open_employer)