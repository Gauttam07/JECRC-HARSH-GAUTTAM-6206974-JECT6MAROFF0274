from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://demoqa.com/browser-windows')

parent_window = driver.current_window_handle

driver.find_element(By.ID, 'tabButton').click()
sleep(2)
windows = driver.window_handles
driver.switch_to.window(windows[1])

assert 'This is a sample page' in driver.find_element(By.ID, 'sampleHeading').text, 'Page not found'

driver.switch_to.window(parent_window)
driver.find_element(By.ID, 'windowButton').click()
sleep(2)
windows = driver.window_handles
driver.switch_to.window(windows[2])

assert 'This is a sample page' in driver.find_element(By.ID, 'sampleHeading').text, 'Page not found'

driver.switch_to.window(parent_window)
driver.find_element(By.ID, 'messageWindowButton').click()
sleep(2)
windows = driver.window_handles
driver.switch_to.window(windows[3])
sleep(5)

driver.quit()
