from selenium import webdriver
from time import sleep

browsers = [ webdriver.Chrome,webdriver.Edge,  webdriver.Firefox]

for browser in browsers:
    driver = browser()
    driver.get("https://www.capgemini.com/")
    driver.maximize_window()
    sleep(2)
    driver.quite()

# webdriver.close()