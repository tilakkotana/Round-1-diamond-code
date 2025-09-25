import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option=Options()
prefs={
    'profile.default_content_setting_values.notifications':2
}
option.add_experimental_option("prefs",prefs)
option.add_argument('--headless')
driver=webdriver.Chrome(options=option)

driver.get('https://testautomationcentral.com/demo/push_notifications.html')
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element(By.XPATH,'//button[@onclick="requestNotificationPermission()"]').click()
print(driver.title)
time.sleep(2)