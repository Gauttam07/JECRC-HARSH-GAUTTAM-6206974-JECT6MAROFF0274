from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Chrome()
driver.get(r"C:\Users\hp5cd\OneDrive\Desktop\capgemniii\ROBO_PY\Selenium\23-March-2026\Adress_form.html")
driver.maximize_window()
sleep(2)
action = ActionChains(driver)

present = driver.find_element(By.ID,'presentAddress')
permanent = driver.find_element(By.ID,'permanentAddress')

present.send_keys("JECRC,JAIPUR,RJ")
sleep(2)
present.click()
action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
sleep(3)
action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
permanent.click()
action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
sleep(2)