from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Chrome()
driver.get(r"C:\Users\hp5cd\OneDrive\Desktop\capgemniii\ROBO_PY\Selenium\23-March-2026\password_action.html")
driver.maximize_window()
sleep(2)
action = ActionChains(driver)

driver.find_element(By.ID, "password").send_keys("nik")
sleep(2)
show_pwd=driver.find_element(By.ID,'eyeBtn')
action.click_and_hold(show_pwd).perform()
sleep(2)
action.release()
