from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://qavbox.github.io/demo/signup/")

wait = WebDriverWait(driver, 10,poll_frequency=500)

driver.maximize_window()

name=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@id="username"]')))
name.send_keys("Dhoom")

email=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@id="email"]')))
email.send_keys("Dhoom@yahoo.com")

Telephone=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@id="tel"]')))
Telephone.send_keys("9876543210")

upload=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@multiple="multiple"]')))
upload.send_keys(r"C:\Users\hp5cd\Downloads\videoframe_18849.png")

gender = wait.until(EC.visibility_of_element_located((By.NAME, "sgender")))
select = Select(gender)
select.select_by_visible_text("Male")

wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='two']"))).click()

wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='automationtesting']"))).click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='java']"))).click()

tool = wait.until(EC.visibility_of_element_located((By.ID, "tools")))
select1 = Select(tool)
select1.select_by_visible_text("Selenium")

wait.until(EC.visibility_of_element_located((By.ID, "submit"))).click()

driver.quit()





