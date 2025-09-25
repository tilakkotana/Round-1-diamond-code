import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/slider/")
driver.maximize_window()
driver.implicitly_wait(2)
f1=driver.find_element(By.XPATH,'//iframe[@class="demo-frame"]')
driver.switch_to.frame(f1)
slider=driver.find_element(By.XPATH,'//div[@id="slider"]')
print(slider.location)
print(slider.size['width'])
print(slider.size['height'])
action=ActionChains(driver)
action.drag_and_drop_by_offset(slider,572,0).perform()
time.sleep(2)
