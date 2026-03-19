from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
sleep(2)

# 1 & 2:
checkbox_link = driver.find_element(By.LINK_TEXT, "Checkboxes")
print(checkbox_link.text)

# 3
drag_drop_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Drag")
print(drag_drop_link.text)

# 4
list_items = driver.find_elements(By.TAG_NAME, "li")
print(len(list_items))

# 5
driver.get("https://the-internet.herokuapp.com/tables")
sleep(2)

# 6
website = driver.find_element(By.XPATH,"//table[@id='table1']//td[text()='jdoe@hotmail.com']/following-sibling::td[1]")
print(website.text)

# 7
delete_btn = driver.find_element(By.XPATH,"//table[@id='table1']//td[text()='Bach']/following-sibling::td//a[text()='delete']")
print(delete_btn.text)

# 8
table2 = driver.find_element(By.XPATH, "(//table)[2]")
print("Second table located")

# 9
cell = driver.find_element(By.XPATH,"//table[@id='table2']//td[text()='$100.00']")
parent_row = cell.find_element(By.XPATH, "./ancestor::tr")

print(cell.text)
print(parent_row.text)

sleep(3)
driver.quit()