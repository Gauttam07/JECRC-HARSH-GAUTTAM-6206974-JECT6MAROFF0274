from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get("https://supertails.com/")
driver.maximize_window()
sleep(2)
action = ActionChains(driver)
cat= driver.find_element(By.XPATH,'//div[@data-ganame="Breed 5"]')
action.scroll_to_element(cat).perform()
# action.click(cat).perform()
# action.context_click(cat).perform()
action.double_click(cat).perform()
sleep(5)


action.scroll_by_amount(0,-1500).perform()
sleep(5)

# action.scroll_from_origin(0,,0,1000).perform()
