from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Настройка опций для headless режима
chrome_options = Options()
chrome_options.add_argument("--headless")

# Инициализация WebDriver с указанием опций
driver = webdriver.Chrome(options=chrome_options)
base_url = 'https://www.saucedemo.com/'

search_result_vakansii_url = 'https://www.superjob.ru/vacancy/search/'
search_result_resume_url = 'https://www.superjob.ru/resume/search_resume.html'
search_result_clients_url = 'https://russia.superjob.ru/clients/'
search_result_kursy_url = 'https://www.superjob.ru/kursy/'

user_resume_url = 'https://www.superjob.ru/user/resume/'
resume_create_url = 'https://www.superjob.ru/resume/create/'

detail_vacancy_page_url = 'https://www.superjob.ru/vakansii/'
detail_resume_page_url = 'https://www.superjob.ru/resume/search_resume.html'
detail_client_page_url = 'https://russia.superjob.ru/clients/'
detail_course_page_url = 'https://www.superjob.ru/kursy/'

employer_login_url = 'https://www.superjob.ru/auth/login/'