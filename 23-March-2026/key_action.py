from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Chrome()
driver.get("https://supertails.com/")
driver.maximize_window()
sleep(2)
action = ActionChains(driver)

# action.send_keys(Keys.PAGE_DOWN).perform()
# sleep(5)
# action.send_keys(Keys.PAGE_UP).perform()
# sleep(5)


action.key_down(Keys.CONTROL).send_keys("a").perform()
sleep(2)
action.key_up(Keys.CONTROL).perform()
sleep(2)
action.key_down(Keys.CONTROL).send_keys("c").perform()
sleep(2)
action.key_up(Keys.CONTROL).perform()

# pasted=action.key_down(Keys.CONTROL).send_keys("d").perform()