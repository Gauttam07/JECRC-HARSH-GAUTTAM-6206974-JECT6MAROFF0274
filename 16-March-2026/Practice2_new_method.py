from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')

driver.maximize_window()

c = driver.find_elements(By.XPATH," //input[@type = 'checkbox' and @class = 'form-check-input']")
for i in c:
    i.click()
    sleep(1)
t = driver.find_elements(By.XPATH,"//input[@type = 'checkbox' and @class = 'form-check-input']/following-sibling::label")
for i in t:
    print(i.text)
for i in c:
    i.click()
    sleep(1)