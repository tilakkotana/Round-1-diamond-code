import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.way2automation.com/way2auto_jquery/resizable.php#load_box')
driver.maximize_window()
driver.implicitly_wait(2)
f1=driver.find_element(By.XPATH,'//iframe[@class="demo-frame"]')
driver.switch_to.frame(f1)
resizable=driver.find_element(By.XPATH,'//div[@id="resizable"]/div[3]')
ActionChains(driver).drag_and_drop_by_offset(resizable,30,30).perform()
time.sleep(1)
