from selenium.webdriver.common.by import By

selection_selector = (By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/form/div[2]/div')
the_search_string = (By.XPATH, '//input[@name="keywords"]')
the_search_button = (By.CSS_SELECTOR, '.f-test-button-Najti')
courses = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[3]/span/a')
select_resume_courses = (By.XPATH, '//div[@id="searchByHintSelect-item-3"]')
filter_specialization_courses = (By.CSS_SELECTOR, ".f-test-clickable-Specializacii")