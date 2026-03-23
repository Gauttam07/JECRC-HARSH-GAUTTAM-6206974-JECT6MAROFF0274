from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# action = ActionChains(driver)
driver.get("https://www.myntra.com/")
driver.maximize_window()
sleep(3)

# men=driver.find_element(By.XPATH,'//a[text()="Men"]')
# sleep(3)
# action.move_to_element(men).perform()
# sleep(2)
# Sports_Shoes=driver.find_element(By.XPATH,"(//a[text()='Sports Shoes'])[1]").click()
# sleep(2)


wait = WebDriverWait(driver,10)
action = ActionChains(driver)

men = wait.until(EC.presence_of_element_located((By.XPATH,'//a[text()="Men"]')))
action.move_to_element(men).perform()

wait.until(EC.presence_of_element_located((By.XPATH,"(//a[text()='Sports Shoes'])[1]"))).click()

four = wait.until(EC.presence_of_element_located((By.XPATH,"(//div[@class='product-sliderContainer'])[11]")))
action.scroll_to_element(four).perform()
sleep(3)