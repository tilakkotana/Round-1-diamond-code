import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
# driver.get("https://www.way2automation.com/way2auto_jquery/alert.php#load_box")
# driver.maximize_window()
# driver.implicitly_wait(1)
# alert=Alert(driver)
# f1=driver.find_element(By.XPATH,'//iframe[@class="demo-frame"]')
# driver.switch_to.frame(f1)
# driver.find_element(By.XPATH,"//button[text()='Click the button to display an alert box:']").click()
# time.sleep(1)
# print(alert.text)
# print(alert.accept())
# time.sleep(1)



driver.get("https://www.way2automation.com/way2auto_jquery/alert.php#load_box")
driver.maximize_window()
driver.implicitly_wait(1)
driver.find_element(By.XPATH,"//a[text()='Input Alert']").click()
f1=driver.find_element(By.XPATH,'//*[@id="example-1-tab-2"]/div/iframe')
driver.switch_to.frame(f1)
driver.find_element(By.XPATH,"//button[text()='Click the button to demonstrate the Input box.']").click()
alert=Alert(driver)
alert.send_keys("Tilak")
alert.accept()
time.sleep(2)
