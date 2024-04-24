from selenium.webdriver.common.by import By

filter_region = (By.CSS_SELECTOR, '.f-test-clickable-Regiony')
the_search_string = (By.XPATH, '//input[@name="keywords"]')
search_vacancy = (By.XPATH, '/html/body/div[1]/div/div[1]/div[4]/div/div[2]/div[1]/div[1]/div/div[1]/div')
the_search_button = (By.CSS_SELECTOR, '.f-test-button-Najti')
otklik_vacancy = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/button')
button_dizlike = (By.CSS_SELECTOR, '.f-test-button-visibility_off')
button_like = (By.XPATH, '//*[@id="app"]/div/div[1]/div[5]/div/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div')
vacancy = (By.XPATH, '/html/body/div[1]/div/div[1]/div[4]/div/div[2]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div/span/a')