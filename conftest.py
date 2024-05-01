
"""Файл с конфигурационными данными для тестов"""

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
import pytest


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


chrome_options = Options()
chrome_options.page_load_strategy = 'eager' #Открываем странцу в режиме запуска "Жаждящий", чтобы не ждать скриптов
chrome_options.add_argument("--headless")
chrome_options.add_argument('log-level=3')



