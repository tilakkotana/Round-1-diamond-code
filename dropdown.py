import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get('https://www.wikipedia.org/')
wait=WebDriverWait(driver,40)
dropdown=driver.find_element(By.XPATH,'//select[@id="searchLanguage"]')
select=Select(dropdown)
select.select_by_value("ast")
time.sleep(1)
select.select_by_index(9)
time.sleep(1)
select.select_by_visible_text('Latina')
time.sleep(1)



##print all languages
total=driver.find_elements(By.XPATH,'//select[@id="searchLanguage"]/option')
print(len(total))
for i in total:
    print(i.get_attribute("lang"))

print('-----------------------------------------------------')
#print all links
block=driver.find_element(By.XPATH,'//nav[@class="other-projects"]')
total=block.find_elements(By.TAG_NAME,'a')
print(total.__getitem__(4).text)
