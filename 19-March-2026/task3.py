from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.amazon.in/")
driver.maximize_window()

wait = WebDriverWait(driver, 15)

search = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
search.send_keys("laptop")

suggestions = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='s-suggestion-container']")))
suggestions[3].click()

# sort = wait.until(EC.element_to_be_clickable((By.ID, "s-result-sort-select")))
# select = Select(sort)
# select.select_by_visible_text("Newest Arrivals")

sort = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='a-dropdown-label']")))
sort.click()

newest = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Newest')]")))
newest.click()

free_shipping = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@id='p_n_free_shipping_eligible/205563695031']/span/a/div")))
free_shipping.click()

first_product = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@data-component-type='s-search-result'])[1]")))

name = first_product.find_element(By.XPATH, '//div[@class="a-section a-spacing-small a-spacing-top-small"]/descendant::span')
price = first_product.find_element(By.XPATH, "//span[@class='a-price-whole']")

print(name.text)
print(price.text)

driver.quit()
