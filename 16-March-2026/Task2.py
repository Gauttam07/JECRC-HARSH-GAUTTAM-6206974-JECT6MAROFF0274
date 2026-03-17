from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Launch browser
driver = webdriver.Chrome()

# 1. Open the website
driver.get("https://demoqa.com/radio-button")
driver.maximize_window()
sleep(2)

# 2. Print page title
print(driver.title)

# 3. Locate "Yes" radio button
yes_radio = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
yes_radio.click()
sleep(2)

# 4. Capture and print result message
result = driver.find_element(By.CLASS_NAME, "text-success")
print("Result Message:", result.text)

# 5. Fetch attributes using get_attribute()
radio_input = driver.find_element(By.ID, "yesRadio")

print( radio_input.get_attribute("id"))
print( radio_input.get_attribute("class"))

# 6. Print current URL
print( driver.current_url)

# Close browser
driver.quit()