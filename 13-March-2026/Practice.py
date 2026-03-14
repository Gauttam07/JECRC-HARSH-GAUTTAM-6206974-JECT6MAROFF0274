from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True )

opts.add_argument('--headless')

driver = webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")


sleep(1)

ID1=driver.find_elements(By.ID,"navbar")
ID2=driver.find_elements(By.ID,"blog-pager")
ID3=driver.find_elements(By.ID,"Wikipedia1")
ID4=driver.find_elements(By.ID,"displayValues")
ID5=driver.find_elements(By.ID,"taskTable")
print(ID1,ID2,ID3,ID4,ID5)
print(len([ID1, ID2, ID3, ID4, ID5]))

class1=driver.find_elements(By.CLASS_NAME,"widget-content")
class2=driver.find_elements(By.CLASS_NAME,"blog-feeds")
class3=driver.find_elements(By.CLASS_NAME,"feed-links")
class4=driver.find_elements(By.CLASS_NAME,"display-values")
class5=driver.find_elements(By.CLASS_NAME,"form-group")
print(class1,class2,class3,class4,class5)
print(len([class1, class2, class3, class4, class5]))


Tag1=driver.find_elements(By.TAG_NAME,"a")
Tag2=driver.find_elements(By.TAG_NAME,"span")
Tag3=driver.find_elements(By.TAG_NAME,"p")
Tag4=driver.find_elements(By.TAG_NAME,"h2")
Tag5=driver.find_elements(By.TAG_NAME,"button")
Tag6=driver.find_elements(By.TAG_NAME,"input")
print('found')
print(len([Tag1, Tag2, Tag3, Tag4, Tag5, Tag6]))


name1=driver.find_elements(By.NAME,"start")
name2=driver.find_elements(By.NAME,"Navbar")
name3=driver.find_elements(By.NAME,"Cross-Column")
name4=driver.find_elements(By.NAME,"Cross-Column 2")
name5=driver.find_elements(By.NAME,"1307673142697428135")
print('found')
print(len([name1, name2, name3, name4, name5]))
driver.quit()