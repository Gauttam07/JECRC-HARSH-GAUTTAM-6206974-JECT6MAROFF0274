from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()
sleep(3)

driver.switch_to.new_window('window')
sleep(5)
driver.get('https://www.cricbuzz.com/')

driver.switch_to.new_window('tab')
sleep(5)
driver.get('https://demo.automationtesting.in/Frames.html')