from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True )

opts.add_argument('--headless')

driver = webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")

sleep(1)

animals=driver.find_elements(By.CSS_SELECTOR,'select[id="animals"]')
print('Nice')

animal=driver.find_element(By.CSS_SELECTOR,'#animals')

find1=driver.find_element(By.CSS_SELECTOR,'a[href*="testautomationpractice"]')
print(find1.get_attribute('href'))

find2=driver.find_element(By.CSS_SELECTOR,'a[href^="http:"]')## find all the elements or attributes have this context starts

# find3=driver.find_elements(By.CSS_SELECTOR,'a[href$=".com"]')## find all the elements or attributes have this context ends
# print(find3.get_attribute('href'))

find3 = driver.find_elements(By.CSS_SELECTOR, 'a[href$=".com"]')

find4= driver.find_elements(By.CSS_SELECTOR, 'div[class="widget-content"]')
print(find1.get_attribute('href'))

find5 = driver.find_elements(By.XPATH, '//input[@placeholder="Enter Name"]')
# print(find1.get_attribute('placeholder'))



print("Total .com links:", len(find3))

for i in find3:
    print(i.get_attribute('href'))

print(find2.get_attribute('href'))

print('worked fine')

Practice1=driver.find_element(By.XPATH, '//h2[@class="title"]')
print(Practice1.get_attribute('text'))
Practice2=driver.find_element(By.XPATH, '//div[@class="display-values"]')
print(Practice2.get_attribute('text'))
Practice3=driver.find_element(By.XPATH, '//div[@class="cap-top"]')
print(Practice3.get_attribute('text'))
Practice4=driver.find_element(By.XPATH, '//label[@for="textbox"]')
print('complete')

InnerText=driver.find_element(By.XPATH, '//a[text()="Home"]')
print(InnerText.get_attribute('text'))

InnerText1=driver.find_element(By.XPATH, '//h2[text()="Pages"]')
print(InnerText1.get_attribute('text'))

InnerText2=driver.find_element(By.XPATH, '//a[text()="PlaywrightPractice"]')
print(InnerText2.get_attribute('text'))

InnerText3=driver.find_element(By.XPATH, '//title[text()="Form Elements"]')
print(InnerText3.get_attribute('text'))

InnerText4=driver.find_element(By.XPATH, '//option[contains(text(),"United States")]')
print(InnerText4.get_attribute('text'))



driver.quit()