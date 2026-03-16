from selenium import webdriver
from time import sleep

driver = webdriver.Edge()

driver.get('http://www.myntra.com/')
driver.maximize_window()
# driver.implicitly_wait(5)
driver.maximize_window()
sleep(1)
driver.get('https://www.capgemini.com/')
sleep(1)
driver.quit()