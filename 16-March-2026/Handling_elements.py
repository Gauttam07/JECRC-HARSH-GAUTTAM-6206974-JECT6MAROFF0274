from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
name=driver.find_element(By.ID,'name')
name.send_keys('Harsh')
email=driver.find_element(By.XPATH,'//input[@placeholder="Enter EMail"]') # locator , locator expression
email.send_keys('Harsh@google.com')

print(name.get_attribute('placeholder'))
print(name.get_attribute('value'))



sleep(5)
print(name)

driver.quit()