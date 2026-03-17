from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

# li=['male','female']
# for i in range(5):
#     for j in li:
#        driver.find_element(By.ID,j).click()
#        sleep(1)

li1=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
for k in li1:
    driver.find_element(By.XPATH,f'//label[text()="{k}"]').click()
    checkbox = driver.find_element(By.XPATH, f'//label[text()="{k}"]')
    print(checkbox.text)
    # print(Checkbox.tex)
    sleep(1)
for l in li1[::-1]:
    driver.find_element(By.XPATH, f'//label[text()="{l}"]').click()
    checkbox = driver.find_element(By.XPATH, f'//label[text()="{l}"]')
    print(checkbox.text)
    sleep(1)



sleep(1)
driver.quit()