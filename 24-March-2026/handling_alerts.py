
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()
# action = ActionChains(driver)
wait = WebDriverWait(driver, 10)
sleep(1)


#simple alert
driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]').click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()
sleep(2)

#confirmation alert
driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]').click()
sleep(2)
alert = driver.switch_to.alert
# alert.accept()
alert.dismiss()
sleep(2)

#prompt alert
driver.find_element(By.XPATH,'//button[@onclick="jsPrompt()"]').click()
sleep(2)
alert = driver.switch_to.alert
alert.send_keys('Happy')
# action.pause(2).perform()
# sleep(5)
alert.accept()
# alert.dismiss()
sleep(2)
