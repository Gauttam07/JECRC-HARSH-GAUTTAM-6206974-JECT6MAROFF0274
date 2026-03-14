from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True )

opts.add_argument('--headless')

driver = webdriver.Chrome(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

sleep(1)

name = driver.find_element(By.ID,"name")
# print(name)

phone_no = driver.find_element(By.ID,'phone')


nav_bar=driver.find_element(By.NAME,"Navbar")
radio_button=driver.find_elements(By.CLASS_NAME,"form-check-input")
print(radio_button)
print(len(radio_button))
inp=driver.find_elements(By.TAG_NAME,'input')
print(len(inp))

# print('name textfield and phone no. found')
print('navbar textfield and phone no. found')


# print('its working fine')
driver.quit()