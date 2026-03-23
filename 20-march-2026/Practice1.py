from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get(r'C:\Users\hp5cd\OneDrive\Desktop\capgemniii\ROBO_PY\Selenium\20-march-2026\playlist.html')
driver.maximize_window()

songs_list=driver.find_element(By.ID,'songs')
select=Select(songs_list)


if select.is_multiple:
    select.select_by_index(4)
    select.select_by_visible_text('Shape of You')
    select.select_by_visible_text('Animals')

print([i.text for i in select.all_selected_options])
print([i.text for i in select.options])

driver.find_element(By.XPATH,'//button[text()="Add to Playlist"]').click()

sleep(2)
driver.quit()