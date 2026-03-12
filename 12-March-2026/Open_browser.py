from selenium import webdriver
from time import sleep

# opts= webdriver.ChromeOptions()
ots=webdriver.FirefoxOptions()
# opts.add_experimental_option()
ots.set_preference("browser.download.folderList",False)
driver = webdriver.Firefox(options=ots)
# opts.add_experimental_option('detach',True)
# driver = webdriver.Chrome(options=opts)



# driver = webdriver.Chrome()
# sleep(5)
# driver= webdriver.Edge()
# driver= webdriver.Firefox()
# sleep(5)

driver.get("https://www.python.org")
driver.maximize_window()

driver.get("https://www.capgemini.com/")
driver.maximize_window()


sleep(5)
# driver.minimize_window()
# sleep(2)
driver.back()
# sleep(2)
driver.forward()
# sleep(2)

print(driver.current_url)
print(driver.title)
print(driver.name)
driver.refresh()
sleep(2)

# driver.quit()
driver.close()

# driver.get("https://www.linkedin.com/")
# driver.maximize_window()
