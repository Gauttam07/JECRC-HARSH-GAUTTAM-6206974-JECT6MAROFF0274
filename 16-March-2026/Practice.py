from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get("https://www.amazon.in/")
sleep(3)
search=driver.find_element(By.XPATH, '//input[@placeholder="Search Amazon.in"]')
search.send_keys("Apple")
search_button=driver.find_element(By.ID, 'nav-search-submit-button')

search_button.click()
sleep(1)
search=driver.find_element(By.XPATH, '//input[@placeholder="Search Amazon.in"]')

search.click()
search.clear()

search=driver.find_element(By.XPATH, '//input[@placeholder="Search Amazon.in"]')
search.send_keys("SAMSUNG S26", Keys.ENTER)
# search_button=driver.find_element(By.ID, 'nav-search-submit-button')
# search_button.click()


sleep(3)
driver.quit()