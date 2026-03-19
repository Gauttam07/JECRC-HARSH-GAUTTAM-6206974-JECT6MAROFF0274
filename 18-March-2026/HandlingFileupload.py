from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)
#
# driver.get("https://the-internet.herokuapp.com/upload")
# driver.maximize_window()
#
# choose_file=driver.find_element(By.ID, "file-upload")
# choose_file.send_keys("C:/Users/hp5cd/Downloads/unnamed.png")
# choose_file.send_keys(r"C:\Users\hp5cd\Downloads\unnamed.png")

# submit_button=driver.find_element(By.ID, "file-submit")
# submit_button.click()
# sleep(2)


driver.get("https://the-internet.herokuapp.com/download")
driver.maximize_window()
driver.find_element(By.XPATH,'//a[text()="Screenshot 2025-12-24 164603.png"]').click()
sleep(10)
print('Download Complete')

driver.quit()