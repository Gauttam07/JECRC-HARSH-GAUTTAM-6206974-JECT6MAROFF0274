from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://codepen.io/gdw96/pen/jOypoYL')

frame = driver.find_element(By.ID, 'result')
driver.switch_to.frame(frame)

user = driver.find_element(By.ID, 'username')
driver.execute_script("arguments[0].value='ABC';", user)

mail = driver.find_element(By.ID, 'email')
driver.execute_script("arguments[0].value='abc@gmail.com';", mail)

pwd = driver.find_element(By.ID, 'password')
driver.execute_script("arguments[0].value='12345679';", pwd)

act = ActionChains(driver)
eye = driver.find_element(By.ID, 'showPsswd')
act.click_and_hold(eye).perform()

sleep(3)

register = driver.find_element(By.XPATH, '//input[@value="Register"]')
register.click()

sleep(5)

driver.switch_to.default_content()
# driver.refresh()
driver.back()

frame = driver.find_element(By.ID, 'result')
driver.switch_to.frame(frame)

heading = driver.find_element(By.TAG_NAME, "h1")
assert 'Registration' in heading.text, "Couldn't find registration page"

print("Registration successful")

driver.close()