# Тут содержаться все локаторы необходимый для тестов со всех страниц
from selenium.webdriver.common.by import By



# Строка поиска, у резюме своя строка
the_search_string = (By.XPATH, '//input[@name="keywords"]')
#  Кнопка Найти в поисковой строке
the_search_button = (By.CSS_SELECTOR, '.f-test-button-Najti')
# селект в строке поиска
selection_selector_client = (By.CSS_SELECTOR, '.f-test-select-searchByHintSelect')
selection_selector = (By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/form/div[2]/div')
#  Кнопка Расширенный поиск у фильтров
button_filter_search = (By.XPATH, '//button[@title="Расширенный поиск"]')


# --------------------------Детальная страница поиска резюме ------------------------------

search_resume = (By.XPATH, '#app .f-test-search-result-item > div:first-child .f-test-link-resume-name')
select_resume_clients = (By.XPATH, '//div[@id="searchByHintSelect-item-2"]')
select_resume_courses = (By.XPATH, '//div[@id="searchByHintSelect-item-3"]')


