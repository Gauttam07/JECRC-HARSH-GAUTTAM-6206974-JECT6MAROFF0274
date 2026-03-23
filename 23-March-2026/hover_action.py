from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get("https://supertails.com/")
driver.maximize_window()
sleep(2)

action= ActionChains(driver)

doggo=driver.find_element(By.XPATH,'(//span[contains(text(),"Dogs")])[1]')
sleep(3)

action.move_to_element(doggo).perform()
sleep(5)

