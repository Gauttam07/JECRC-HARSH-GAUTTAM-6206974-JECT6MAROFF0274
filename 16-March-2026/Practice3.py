from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://www.flipkart.com/')
driver.maximize_window()
sleep(2)

cross= driver.find_element(By.XPATH,'//span[@role="button"]').click()

search=driver.find_element(By.XPATH,"//input[@name='q']")
sleep(2)
search.clear()
search.send_keys('Mobile',Keys.ENTER)
search=driver.find_element(By.XPATH,"//input[@name='q']")
x=search.get_attribute('value')
print(x)
sleep(2)
checkbox = driver.find_element(By.XPATH,"//div[text() = 'Apple']/preceding-sibling::div")
checkbox.click()
ch=driver.find_element(By.XPATH,"//div[text() = 'Apple']")
print(ch.text)
sleep(1)

# abc=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div/div/img')
img=driver.find_element(By.XPATH,'//div[@class="lWX0_T"]/img')
print(img.get_attribute('src'))
sleep(2)
driver.quit()
