"""Страница с методами, которые буду общими для всех страниц"""
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

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

    def is_enabled(self):
        return self.browser.is_enabled()

    def wait(self):
        wait = WebDriverWait(self.browser, 10)
        return self.wait
        # return self.browser.WebDriverWait(self.browser, 10).until(args)

