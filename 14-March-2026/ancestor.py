from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_argument('--headless')

driver = webdriver.Chrome(options=opts)
# driver.get("https://www.amazon.in/")
driver.get("https://testautomationpractice.blogspot.com/")
# sleep(1)

# sp1 = driver.find_elements(By.XPATH, "//span[text()='ALL']/ancestor::div[@id='nav-main']")
# sp2 = driver.find_elements(By.XPATH,"//div[@id='nav-main']/descendant::span[text()='All']")
# sp3 = driver.find_elements(By.XPATH,"//a[text()='Fresh']/ancestor::li/following::li[1]")
# print('completed')

driver.find_elements(By.LINK_TEXT,"Udemy Courses")
print('i found the element using link text')

driver.find_elements(By.PARTIAL_LINK_TEXT,"Udemy Courses")
print('i found the element using partial-link')

