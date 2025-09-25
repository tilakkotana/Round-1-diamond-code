import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.way2automation.com/way2auto_jquery/droppable.php#load_box")
driver.maximize_window()
driver.implicitly_wait(2)
f1=driver.find_element(By.XPATH,'//iframe[@class="demo-frame"]')
driver.switch_to.frame(f1)
draggable=driver.find_element(By.XPATH,'//div[@id="draggable"]')
droppable=driver.find_element(By.XPATH,'//div[@id="droppable"]')
ActionChains(driver).drag_and_drop(draggable,droppable).perform()
time.sleep(1)
