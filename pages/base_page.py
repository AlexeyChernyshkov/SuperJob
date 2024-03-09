"""Страница с методами, которые буду общими для всех страниц"""

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
        return self.is_displayed()

