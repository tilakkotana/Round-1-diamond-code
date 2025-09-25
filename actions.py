import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://www.way2automation.com/")
driver.maximize_window()
wait=WebDriverWait(driver,60)
menu=driver.find_element(By.XPATH,'//span[text()="Resources"]')
action=ActionChains(driver)
action.move_to_element(menu).perform()
driver.find_element(By.XPATH,"//span[text()='Practice Site 1']").click()
time.sleep(3)
