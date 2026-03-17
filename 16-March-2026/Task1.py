from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Launch browser
driver = webdriver.Chrome()

# 1. Open the website
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
sleep(2)

# 2. Print page title
print( driver.title)

# 3. Locate username field and clear
username = driver.find_element(By.NAME, "username")
username.clear()
username.send_keys("Admin")

# 4. Locate password field and enter password
password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")
sleep(1)
# 5. Submit login (using click)
login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
login_btn.click()

sleep(3)

# 6. Print current URL
current_url = driver.current_url
print("Current URL:", current_url)
sleep(1)
# 7. Verify dashboard
if "dashboard" in current_url:
    print("successful login")
else:
    print("login failed")

# Close browser
driver.quit()