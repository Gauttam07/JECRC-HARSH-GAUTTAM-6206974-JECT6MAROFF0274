from selenium import webdriver
from time import sleep

browsers = [webdriver.Chrome,webdriver.Edge,webdriver.Firefox]

for browser in browsers:
    driver = browser()
    driver.get("https://www.capgemini.com/")
    driver.maximize_window()
    print(driver.current_url)
    print(driver.title)
    print(driver.name)
    # print(driver.page_source)
    sleep(2)
    driver.quit()


