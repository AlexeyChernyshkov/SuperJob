"""Страница с методами, которые буду общими для всех страниц"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import *


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        # self.driver = driver

    def open(self):
        self.browser.get(self.url)

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

    def wait_text_in_element(self, locator, string):
        return WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element(locator, string))

    def wait_element_to_be_clickable(self, locator):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))

    def wait_visibility_of_element_located(self, locator):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator))

    def wait_presence_of_element_located(self, locator):
        return WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))

    def wait_url_matches(self, url):
        return WebDriverWait(self.browser, 10).until(EC.url_matches(url))

    def top_button_login(self):
        return self.find(top_button_login)

    def notifications(self):
        return self.find(notifications)

    def top_account(self):
        return self.find(top_account)

    def save_screenshot(self, file_name: str):
        return self.browser.save_screenshot(f"screenshots/{file_name}.png")

    def script_click(self, element):
        return self.browser.execute_script("arguments[0].click();", element)

    def script_scroll(self, element):
        return self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_value(self, locator):
        return self.browser.find_element(*locator).get_attribute("value")

    def window_handles(self):
        return self.browser.window_handles

    def switch_to_window(self, handle):
        return self.browser.switch_to.window(handle)


