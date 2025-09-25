import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://deluxe-menu.com/popup-mode-sample.html')
driver.maximize_window()
driver.implicitly_wait(2)
img=driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td[3]/p[2]/img')

ActionChains(driver).context_click(img).perform()
img=driver.find_element(By.XPATH,"//td[text()='Product Info']")
ActionChains(driver).context_click(img).perform()
img=driver.find_element(By.XPATH,"//td[text()='Installation']")
ActionChains(driver).context_click(img).perform()
driver.find_element(By.XPATH,"//td[text()='How To Setup']").click()
time.sleep(2)
