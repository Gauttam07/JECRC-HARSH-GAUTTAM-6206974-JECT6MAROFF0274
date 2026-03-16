from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_argument('--headless')

driver = webdriver.Chrome(options=opts)
# driver.get("https://www.amazon.in/")
driver.get("https://testautomationpractice.blogspot.com/")


driver.find_elements(By.XPATH,"//td[text()='Learn Java']/following-sibling::td[3]")

driver.find_elements(By.XPATH,"//td[text()='Amod']/ancestor::tbody/descendant::tr[2]/td[3]")

sp1=driver.find_elements(By.XPATH,"//td[text()='300']/preceding-sibling::td[3]")
for el in sp1:
    print(el.text)
sp2=driver.find_elements(By.XPATH,"//table[@id='taskTable']/descendant::tbody[@id='rows']/descendant::tr/td[1]")
for el in sp2:
    print(el.text)

