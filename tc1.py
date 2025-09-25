# Test Case
# -----------
# 1) Open Web Browser(Chrome/firefox/Edge).
# 2) Open URL  https://opensource-demo.orangehrmlive.com/
# 3) Enter username  (Admin).
# 4) Enter password  (admin123).
# 5) Click on Login.
# 6) Capture title of the home page.(Actual title)
# 7) Verify title of the page: OrangeHRM    (Expected)
# 8) close browser


import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

start=time.time()

driver=webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver,60)
driver.get("https://opensource-demo.orangehrmlive.com/")
wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//input[@name="username"]'))).send_keys("Admin")
wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//input[@name="password"]'))).send_keys("admin123")
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(4)
act_title=driver.title
exp_title="OrangeHRM"

#assert act_title==exp_title,"Title Not matching"

if act_title==exp_title:
    print("Test case passed")
else:
    print("Title Not matching")

end=time.time()
print(round(end-start,2))
driver.close()

