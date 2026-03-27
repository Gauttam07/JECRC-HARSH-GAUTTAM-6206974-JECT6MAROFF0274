from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://demoqa.com/alerts')

driver.find_element(By.ID, 'alertButton').click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()

wait = WebDriverWait(driver, 5)
driver.find_element(By.ID, 'timerAlertButton').click()
sleep(2)
alert = wait.until(EC.alert_is_present())
alert.accept()

driver.find_element(By.ID, 'confirmButton').click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()

res1 = driver.find_element(By.XPATH, '(//div[@class="col-md-6"])[3]/span[2]')
assert 'Ok' in res1.text, 'Error'

driver.find_element(By.ID, 'confirmButton').click()
sleep(2)
alert = driver.switch_to.alert
alert.dismiss()

res2 = driver.find_element(By.XPATH, '(//div[@class="col-md-6"])[3]/span[2]')
assert 'Cancel' in res2.text, 'Error'

driver.find_element(By.ID, 'promtButton').click()
alert = driver.switch_to.alert
sleep(2)
alert.send_keys('Hello')
alert.accept()

res3 = driver.find_element(By.ID, 'promptResult')
assert 'Hello' in res3.text, 'Error'

driver.find_element(By.ID, 'promtButton').click()
sleep(2)
alert = driver.switch_to.alert
alert.dismiss()
driver.close()