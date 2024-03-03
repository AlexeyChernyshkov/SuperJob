from config import *
from pages.users import *
import pytest
import time
from pages.locators import *


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(base_url)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_open_page(browser):
    # create_resume_button = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div[1]/div[2]/div/div[1]/div/a/span')
    print("OK")


