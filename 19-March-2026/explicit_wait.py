from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)

driver.get("http://abc.com/")

wait_obj = WebDriverWait(driver, 10,poll_frequency=200)

# submit_button=wait_obj.until(EC.element_to_be_clickable((By.ID,'button')))
# submit_button.click()



driver.quit()