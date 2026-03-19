from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
sleep(2)

# Fill First Name
driver.find_element(By.ID, "firstName").send_keys("Harsh")


sleep(1)
driver.find_element(By.ID, "lastName").send_keys("Gauttam")


sleep(2)
driver.find_element(By.ID, "userEmail").send_keys("harsh123@gmail.com")


sleep(2)
driver.find_element(By.XPATH, "//label[text()='Male']").click()


sleep(2)
driver.find_element(By.ID, "userNumber").send_keys("9876543210")


sleep(2)
subject = driver.find_element(By.ID, "subjectsInput")
subject.send_keys("Maths")
subject.send_keys(Keys.ENTER)


sleep(2)
driver.find_element(By.XPATH, "//label[text()='Sports']").click()
driver.find_element(By.XPATH, "//label[text()='Reading']").click()

sleep(2)
driver.find_element(By.ID, "uploadPicture").send_keys(r"C:\Users\hp5cd\Downloads\videoframe_18849.png")

sleep(5)
driver.find_element(By.ID, "currentAddress").send_keys("Jaipur, Rajasthan")


sleep(2)
driver.find_element(By.ID, "react-select-3-input").send_keys("NCR")
driver.find_element(By.ID, "react-select-3-input").send_keys(Keys.ENTER)


sleep(2)
driver.find_element(By.ID, "react-select-4-input").send_keys("Delhi")
driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.ENTER)


sleep(5)
submit=driver.find_element(By.ID, "submit")
submit.click()
print('submitted')

sleep(3)
driver.quit()