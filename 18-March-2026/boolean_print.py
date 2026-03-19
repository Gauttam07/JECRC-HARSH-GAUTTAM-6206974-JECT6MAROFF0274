from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

radio=driver.find_element(By.ID,'male')
radio.click()

print(radio.is_displayed())
print(radio.is_enabled())

sleep(3)
checkbox=driver.find_element(By.XPATH, '//label[text()="Monday"]/preceding-sibling::input')
print(checkbox.is_displayed())
checkbox.click()


print(checkbox.is_selected())

# monday_checkbox=driver.find_element(By.XPATH, '//input[@id="monday"]/following-sibling::label')
# print(monday_checkbox.text)

sleep(3)
driver.quit()