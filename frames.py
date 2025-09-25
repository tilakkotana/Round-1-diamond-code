from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_prompt")
driver.maximize_window()
driver.implicitly_wait(1)
f1=driver.find_element(By.XPATH,"//iframe[@id='iframeResult']")
driver.switch_to.frame(f1)
driver.find_element(By.XPATH,"//button[text()='Try it']").click()
alert=Alert(driver)
alert.accept()
time.sleep(1)
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//button[@id='runbtn']").click()
time.sleep(5)

