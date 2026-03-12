from selenium import webdriver
from time import sleep

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.capgemini.com/")

driver.maximize_window()


sleep(5)

driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(2)
driver.minimize_window()
sleep(2)
driver.close()

