import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

folder = os.path.join(os.getcwd(),'Screenshots')
os.makedirs(folder,exist_ok=True)

driver = webdriver.Chrome()

action = ActionChains(driver)
driver.get('https://www.marvel.com/movies/blade')
driver.get('https://in.pinterest.com/')

driver.maximize_window()
sleep(2)
# sleep(2)
#
# driver.save_screenshot(f"{folder}/full_scr.png")
# sleep(2)

ele=driver.find_element(By.XPATH,"(//div[@class='ADXRXN AsRsEE'])[3]/descendant::img")
action.scroll_to_element(ele).perform()
sleep(2)
ele.screenshot(f"{folder}/cherry_red.png")
sleep(2)