from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.way2automation.com/way2auto_jquery/automation-practice-site.html")
driver.maximize_window()
driver.implicitly_wait(2)
print(driver.find_element(By.XPATH,'//h3').value_of_css_property('font-family'))
print(driver.find_element(By.XPATH,'//h3').value_of_css_property('font-size'))