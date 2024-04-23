from selenium.webdriver.common.by import By

the_search_string_resume = (By.XPATH, '//input[@name="keywords[0][keys]"]')
the_search_button = (By.CSS_SELECTOR, '.f-test-button-Najti')
resume = (By.CSS_SELECTOR, '#app .f-test-search-result-item > div:first-child .f-test-link-resume-name')
selection_selector = (By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/form/div[2]/div')
select_resume = (By.XPATH, '//div[@id="searchByHintSelect-item-1"]')
