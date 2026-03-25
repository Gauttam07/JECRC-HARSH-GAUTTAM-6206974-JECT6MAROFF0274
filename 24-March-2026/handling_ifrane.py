
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()
sleep(3)

#single-iframe Handling
iframe=driver.find_element(By.ID,'singleframe')
driver.switch_to.frame(iframe)
sleep(2)
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('123')
sleep(2)

driver.switch_to.default_content()

#nested iframe handling
driver.find_element(By.XPATH,'//a[text()="Iframe with in an Iframe"]').click()
sleep(2)
iframe=driver.find_element(By.XPATH,'//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(iframe)

iframe=driver.find_element(By.XPATH,'//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(iframe)
sleep(2)
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('123')
sleep(2)
driver.switch_to.parent_frame()
driver.switch_to.parent_frame()
sleep(2)
driver.find_element(By.XPATH,'//a[text()="Single Iframe "]').click()

