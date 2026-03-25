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

parent_window = driver.current_window_handle # when use multiple window we prefer to use less

driver.find_element(By.XPATH,'//a[text()="Click Here"]').click()
sleep(1)
all_windows = driver.window_handles
print(len(all_windows))

driver.switch_to.window(all_windows[-1])
print(driver.find_element(By.CLASS_NAME,'example').text)

assert 'New'in driver.find_element(By.CLASS_NAME,'example').text
print('done')
driver.switch_to.window(parent_window)
sleep(3)