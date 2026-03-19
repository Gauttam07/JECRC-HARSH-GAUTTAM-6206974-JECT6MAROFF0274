from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)

driver.get("https://abc.com/")
driver.maximize_window()
driver.implicitly_wait(5)

ele=driver.find_element(By.XPATH,'(//a[@class="AnchorLink"]/parent::li/descendant::img)[1]')
print(ele.get_attribute('src'))

driver.quit()