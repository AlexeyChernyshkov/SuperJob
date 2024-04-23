"""Страница с методами, которые буду общими для всех страниц"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from locators.common_locators import *


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        # self.driver = driver

    '''Основные методы'''
    def open(self):
        self.browser.get(self.url)

    def close(self):
        self.browser.close()

    def quit(self):
        self.browser.quit()

    def find(self, args):
        return self.browser.find_element(*args)

    @property
    def is_displayed(self):
        return self.browser.is_displayed()

    def text(self):
        return self.browser.text()

    def send_keys(self, args):
        return self.browser.send_keys(args)

    def click(self):
        return self.browser.click()

    def clear(self):
        return self.browser.clear()

    def is_enabled(self):
        return self.browser.is_enabled()

    def save_screenshot(self, file_name: str):
        return self.browser.save_screenshot(f"screenshots/{file_name}.png")

    def script_click(self, element):
        return self.browser.execute_script("arguments[0].click();", element)

    def script_scroll(self, element):
        return self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_value(self, locator):
        return self.browser.find_element(*locator).get_attribute("value")

    def get_href(self, locator):
        return self.browser.find_element(*locator).get_attribute("href")

    @staticmethod
    def cut_string(string):
        return string[string.find(".") + 1:]

    '''Waits'''
    def wait_text_in_element(self, locator, string):
        return WebDriverWait(self.browser, 5).until(EC.text_to_be_present_in_element(locator, string))

    def wait_element_to_be_clickable(self, locator):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(locator))

    def wait_visibility_of_element_located(self, locator):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))

    def wait_presence_of_element_located(self, locator):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(locator))

    def wait_url_matches(self, url):
        return WebDriverWait(self.browser, 5).until(EC.url_matches(url))

    def wait_text_to_be_present_in_element_value(self, locator, string):
        return WebDriverWait(self.browser, 5).until(EC.text_to_be_present_in_element_value(locator, string))

    def wait_visibility_of(self, element):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of(element))

    def implicitly_wait(self):
        return self.browser.implicitly_wait(5)

    '''Взаимодействие с браузером'''
    # def session_id(self):
    #     return self.browser.session_id

    def window_handles(self):
        return self.browser.window_handles

    def switch_to_window(self, handle):
        return self.browser.switch_to.window(handle)

    def action(self):
        return ActionChains(self.browser)

    def current_url(self):
        return self.browser.current_url

    def open_in_new_tab(self, element):
        return self.action().move_to_element(element).key_down(Keys.LEFT_CONTROL).click().key_up(Keys.LEFT_CONTROL).perform()

    def get_page_url(self):
        handles = self.window_handles()
        if len(handles) == 1:
            url = self.current_url()
            return url
        else:
            page = handles[1]
            self.switch_to_window(page)
            url = self.current_url()
            return url

    def compare_url(self, locator):
        href = self.get_href(locator)
        element = self.find(locator)
        self.open_in_new_tab(element)
        url = self.get_page_url()
        self.close()
        self.switch_to_window(self.window_handles()[0])
        href_2 = self.cut_string(href)
        url_2 = self.cut_string(url)
        if href_2 == url_2:
            return True
        else:
            return False

