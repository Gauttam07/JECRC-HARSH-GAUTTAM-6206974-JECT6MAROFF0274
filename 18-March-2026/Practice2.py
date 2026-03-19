from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)
# driver = webdriver.Chrome()
driver.get("https://www.lenskart.com/")
# driver.get("https://www.lenskart.com/lenskart-blu-lb-e14789-c1-eyeglasses.html")
driver.maximize_window()
sleep(2)

search=driver.find_element(By.XPATH,"//input[@class='aa-Input']")
search.click()
sleep(2)
search.send_keys("classics",Keys.ENTER)
sleep(2)

sorting=driver.find_element(By.ID,'sortByDropdown')
dropdown=Select(sorting)
dropdown.select_by_value("saving")
sleep(2)
find=driver.find_element(By.XPATH,"//div[@class='sc-23b7d3eb-6 hYdmOJ']/div/following-sibling::p")
print(find.text)

driver.quit()




























































































