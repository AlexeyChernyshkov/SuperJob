from config import *
from pages.users import *
import pytest
import time
# from pages.locators import *
# from pages.users import *
from pages.resume_create import ResumeCreate


# from selenium.webdriver.support.wait import WebDriverWait


def test_input_name(browser):
    print("1")
    resume_create = ResumeCreate(browser, resume_create_url)
    print("2")
    resume_create.open()
    print("3")
    browser.implicitly_wait(5)
    print("4")
    resume_create.field_input()
    print("5")
