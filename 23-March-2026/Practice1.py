from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=opts)
driver.get('https://demoqa.com/droppable')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# origin_ele=driver.find_element(By.ID,'draggable')
# target_ele=driver.find_element(By.ID,'droppable')
origin_ele = wait.until(EC.visibility_of_element_located((By.ID, 'draggable')))
target_ele = wait.until(EC.visibility_of_element_located((By.ID, 'droppable')))

actions = ActionChains(driver)
sleep(5)
actions.drag_and_drop(origin_ele, target_ele).perform()
assert 'Dropped' == target_ele.text,'Not Done'
print('Done Perfect')
driver.quit()
