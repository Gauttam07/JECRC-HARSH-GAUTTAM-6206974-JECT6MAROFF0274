from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)
# driver = webdriver.Chrome()
# driver.get("https://www.lenskart.com/")
driver.get("https://www.lenskart.com/lenskart-blu-lb-e14789-c1-eyeglasses.html")
driver.maximize_window()

sleep(5)

driver.find_element(By.XPATH, "//button[@class='sc-39b66eee-0 boDzrJ']").click()

check=driver.find_element(By.XPATH, "//div[@class='sc-a3b31f26-14 fDEfLM']")
assert check.is_displayed()

# eyeglass=driver.find_element(By.ID,'lrd1')
# # print(eyeglass.text)
#
# assert 'EYEGLASS' == eyeglass.text,'did not show EYEGLASSES'
# print('success')


driver.quit()