
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
    # driver.save_screenshot("test.png")
    driver.quit()


chrome_options = Options()
chrome_options.page_load_strategy = 'eager' #Открываем странцу в режиме запуска "Жаждящий", чтобы не ждать скриптов
# chrome_options.add_argument("--headless")
chrome_options.add_argument('log-level=3')



base_url = 'https://www.superjob.ru/'

search_result_vacancy_url = 'https://www.superjob.ru/vacancy/search/'
search_result_resumes_url = 'https://www.superjob.ru/resume/search_resume.html'
search_result_clients_url = 'https://russia.superjob.ru/clients/'
search_result_courses_url = 'https://www.superjob.ru/kursy/'

user_resume_url = 'https://www.superjob.ru/user/resume/'
# resume_create_url = 'https://www.superjob.ru/resume/create/'

detail_vacancy_page_url = 'https://www.superjob.ru/vakansii/'
detail_resume_page_url = 'https://www.superjob.ru/resume/search_resume.html'
detail_client_page_url = 'https://russia.superjob.ru/clients/'
detail_course_page_url = 'https://www.superjob.ru/kursy/'

employer_login_url = 'https://www.superjob.ru/auth/login/'

