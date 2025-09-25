# Assignment
# -----------
# 1) Open Web Browser(Chrome/firefox/IE).
# 2) Open URL  https://admin-demo.nopcommerce.com/login
# 3) Provide Email  (admin@yourstore.com).
# 4) Provide password  (admin).
# 5) Click on Login.
# 6) Capture title of the dashboard page.(Actual title)
# 7) Verify title of the page: "Dashboard / nopCommerce administration" (Expected)
# 8) close browser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
driver=webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver,60)
driver.get("https://admin-demo.nopcommerce.com/login")
wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//input[@type="email"]'))).clear()
driver.find_element(By.XPATH,'//input[@type="email"]').send_keys("admin@yourstore.com")
driver.find_element(By.XPATH,'//input[@type="password"]').clear()
time.sleep(1)
driver.find_element(By.XPATH,'//input[@type="password"]').send_keys("admin")
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(4)
act_title=driver.title
exp_title="Dashboard / nopCommerce administration"
assert act_title==exp_title,"Title not matching"
driver.close()
