from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.way2automation.com/way2auto_jquery/frames-and-windows.php#load_box")
driver.maximize_window()
driver.implicitly_wait(1)




# f1=driver.find_element(By.XPATH,'//div[@id="example-1-tab-1"]/div/iframe')
# driver.switch_to.frame(f1)
# driver.find_element(By.XPATH,"//a[text()='New Browser Tab']").click()
# time.sleep(1)
# driver.find_element(By.XPATH,"//a[text()='New Browser Tab']").click()
# time.sleep(1)
# windows=driver.window_handles
# driver.switch_to.window(windows[2])
# driver.close()
# time.sleep(1)
# driver.switch_to.window(windows[1])
# driver.close()
# time.sleep(1)
# driver.switch_to.window(windows[0])
# driver.close()
# time.sleep(1)



driver.find_element(By.XPATH,"//a[text()='Open Seprate New Window']").click()
f1=driver.find_element(By.XPATH,'//div[@id="example-1-tab-2"]/div/iframe')
driver.switch_to.frame(f1)
driver.find_element(By.XPATH,"//a[text()='Open New Seprate Window']").click()
time.sleep(1)
windows=driver.window_handles
driver.switch_to.window(windows[1])
driver.close()
time.sleep(1)
driver.switch_to.window(windows[0])
driver.close()
time.sleep(1)


