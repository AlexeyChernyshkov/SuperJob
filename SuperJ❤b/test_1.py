from config import *
from pages.users import *
import pytest
import time
from pages.locators import *
from pages.users import *
from pages.users import *


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(base_url)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


