from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://abc.com/')

wait = WebDriverWait(driver, 10)

IMG_links = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//section[@class="tilegroup tilegroup--homehero tilegroup--landscape"]/descendant::img')))
for i in IMG_links:
    print('IMG LINK')
    print(i.get_attribute('src'))

driver.quit()